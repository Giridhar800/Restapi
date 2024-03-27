from django.contrib import admin
from django.urls import path
from restapp6 import views

urlpatterns =[
    path('custmorlist/', views.CustomerList.as_view()),
    path('custmorcreate/', views.CustomerCreate.as_view()),
    path('custmorretrieve/<int:pk>', views.CustomerRetrieve.as_view()),
    path('custmorupdate/<int:pk>', views.CustomerUpdate.as_view()),
    path('custmordelete/<int:pk>', views.CustomerDelete.as_view()),
    path('RUD/<int:pk>', views.Retrive_Update_Delete.as_view()),
    path('LC/', views.List_Create.as_view()),

]