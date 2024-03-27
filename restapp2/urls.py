from django.urls import path
from restapp2 import views

urlpatterns = [
    path('emp/<int:pk>', views.emp_details),
    path('empall/', views.emp_all_details),
]