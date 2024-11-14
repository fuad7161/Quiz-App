from django.urls import path
from .views import QuestionListView, QuestionDetailView, SubmitAnswerView, PracticeHistoryView

urlpatterns = [
    path('questions/', QuestionListView.as_view(), name='question-list'),
    path('questions/<str:question_id>/', QuestionDetailView.as_view(), name='question-detail'),
    path('questions/<str:question_id>/submit/', SubmitAnswerView.as_view(), name='submit-answer'),
    path('users/<str:user_id>/practice-history/', PracticeHistoryView.as_view(), name='practice-history'),
]
