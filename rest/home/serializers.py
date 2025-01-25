from rest_framework import serializers
from .models import Question, Answer
from .custom_relational_fields import CustomUserRelationalFields


class QuestionSerializer(serializers.ModelSerializer):
    user = CustomUserRelationalFields(read_only=True)
    answers = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ('id', 'user', 'title', 'slug', 'content', 'answers', 'likes')
        extra_kwargs = {
            'slug': {'read_only': True},
        }

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def get_answers(self, obj):
        result = obj.answers.all()
        ser_data = AnswerSerializer(instance=result, many=True).data
        return ser_data

    def get_likes(self, obj):
        result = obj.votes.count()
        return result


class AnswerSerializer(serializers.ModelSerializer):
    user = CustomUserRelationalFields(read_only=True)

    class Meta:
        model = Answer
        fields = '__all__'
