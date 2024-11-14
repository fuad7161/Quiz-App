from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Question, Submission, PracticeHistory, Option
from .serializers import QuestionSerializer, SubmissionSerializer, PracticeHistorySerializer

class QuestionListView(APIView):
    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class QuestionDetailView(APIView):
    def get(self, request, question_id):
        try:
            question = Question.objects.get(id=question_id)
            serializer = QuestionSerializer(question)
            return Response(serializer.data)
        except Question.DoesNotExist:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)

class SubmitAnswerView(APIView):
    def post(self, request, question_id):
        try:
            question = Question.objects.get(id=question_id)
            option_id = request.data.get("selected_option")
            selected_option = Option.objects.get(id=option_id, question=question)
            is_correct = selected_option.is_correct

            submission = Submission.objects.create(
                user_id=request.data.get("user_id"),
                question=question,
                selected_option=selected_option,
                is_correct=is_correct
            )
            return Response({"message": "Answer submitted successfully.", "is_correct": is_correct})
        except (Question.DoesNotExist, Option.DoesNotExist):
            return Response({"error": "Invalid question or option"}, status=status.HTTP_400_BAD_REQUEST)

class PracticeHistoryView(APIView):
    def get(self, request, user_id):
        try:
            history = PracticeHistory.objects.get(user_id=user_id)
            serializer = PracticeHistorySerializer(history)
            return Response(serializer.data)
        except PracticeHistory.DoesNotExist:
            return Response({"error": "Practice history not found"}, status=status.HTTP_404_NOT_FOUND)
