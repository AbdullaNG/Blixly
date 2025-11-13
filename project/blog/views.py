from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def home(request):
	context = {'posts': Post.objects.all()}
	return render(request, 'blog/index.html', context)

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


class PostDetailView(DetailView):
	model = Post


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
	success_url = reverse_lazy('blog-home')

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

	def get_context_data(self, **kwargs):
		return super().get_context_data(**kwargs)


def about(request):
	return render(request, 'blog/about.html')
