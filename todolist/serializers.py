from rest_framework import serializers

from rest_framework import serializers
from todolist.models import Task, Comment, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    # создаем класс наследник от базового класса сериализатор на основе модели
    comments_count = serializers.SerializerMethodField()
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task  # указываем модель, для которой будут сериализаваться и десериализоваться данные
        # fields = '__all__'  # указываем набор полей, с которыми будем работать при сериализации и десериализации
        fields = ['title', 'description', 'deadline', 'completed', 'comments_count', 'tags', 'comments']

    def get_comments_count(self, obj):
        return obj.comments.count()
