from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	date_posted = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name='likes', blank=True)

	def number_of_likes(self):
		return self.likes.count()

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})


class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']


	def __str__(self):
		return f'Comment by {self.author} on {self.post}'

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})