from rest_framework.serializers import ModelSerializer
from blog.models import Post, Comment
from users.models import Profile
from django.contrib.auth.models import User


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['author', 'date_posted', 'likes']


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['author', 'created_at']


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ['image']