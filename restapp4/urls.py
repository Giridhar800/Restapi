from django.urls import path
from restapp4 import views

urlpatterns = [
    path('trainer/', views.trainer_api),

]