from rest_framework import serializers
from .models import User, Category, Tag, Task, Subtask

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'color']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ['id', 'description', 'is_completed']

class TaskSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    tag_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Tag.objects.all(), source='tags', required=False)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'status', 'category', 'tags', 'tag_ids']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        tags = validated_data.pop('tags', [])
        task = Task.objects.create(**validated_data)
        task.tags.set(tags)
        return task

    def update(self, instance, validated_data):
        tags = validated_data.pop('tags', None)
        task = super().update(instance, validated_data)
        if tags is not None:
            task.tags.set(tags)
        return task
