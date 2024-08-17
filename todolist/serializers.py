from rest_framework import serializers
from todolist.models import Task, Comment, Tag

from .utils import get_cached_tags


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    comments_count = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        # fields = '__all__'
        fields = ['title', 'description', 'deadline', 'completed', 'comments_count', 'tags', 'comments']

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_tags(self, obj):
        tags = get_cached_tags(obj.id)
        return [tag.name for tag in tags]
