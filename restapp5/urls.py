from django.urls import path
from restapp5 import views

urlpatterns = [
    path('manager/', views.ManagerAPI.as_view()),
    path('manager/<int:pk>', views.ManagerAPI.as_view()),

]