from django.urls import path
from .views import UniversityAPIView, StudentAPIView,StudentDetailAPIView,UniversityDetailAPIView


urlpatterns = [
    path('university/', UniversityAPIView.as_view()),
    path('universitydetail/<int:id>/', UniversityDetailAPIView.as_view()),
    path('student/', StudentAPIView.as_view()),
    path('studentdetail/<int:id>/', StudentDetailAPIView.as_view()),

]
