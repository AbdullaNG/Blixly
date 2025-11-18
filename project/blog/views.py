from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class PostListView(ListView):
	model = Post
	template_name ='blog/index.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5


class PostsListView(ListView):
	model = Post
	template_name ='blog/posts.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 5


def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	comments = post.comments.all()
	new_comment = None
	
	if request.method == 'POST':
		comment_form = CommentForm(request.POST)

		if comment_form.is_valid():
			new_comment = comment_form.save(commit=False)
			new_comment.post = post
			new_comment.author = request.user
			new_comment.save()
			return redirect('post-detail', pk=post.pk)

	comment_form = CommentForm()
	context = {'post': post, 'comments': comments, 'comment_form': comment_form, 'new_comment': new_comment}

	return render(request, 'blog/post_detail.html', context)



class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']
	template_name = 'blog/post_create.html'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']
	template_name = 'blog/post_update.html'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('posts')

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

	def get_context_data(self, **kwargs):
		return super().get_context_data(**kwargs)


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Comment
	success_url = reverse_lazy('posts')

	def test_func(self):
		comment = self.get_object()
		if self.request.user == comment.author:
			return True
		return False

	def get_context_data(self, **kwargs):
		return super().get_context_data(**kwargs)


def about(request):
	return render(request, 'blog/about.html')
