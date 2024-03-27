from django.urls import path
from restapp1 import views

urlpatterns = [
    path('emp/', views.empdetails.as_view()),
]