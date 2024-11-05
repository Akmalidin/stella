from django.urls import path
from .views import FeedbackList, FeedbackDetail

urlpatterns = [
    path('', FeedbackList.as_view(), name='feedback'),
    path('<int:pk>/', FeedbackDetail.as_view(), name='feedback-detail'),
]