from django.urls import path
from restapp3 import views

urlpatterns = [
    path('emp/', views.empdata.as_view()),

]