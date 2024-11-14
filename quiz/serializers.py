from rest_framework import serializers
from .models import User, Question, Option, Submission, PracticeHistory

class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'text', 'options']

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['user', 'question', 'selected_option', 'is_correct']

class PracticeHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PracticeHistory
        fields = ['user', 'total_questions', 'correct_answers']
