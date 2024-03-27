from django.contrib import admin
from django.urls import path
from restapp7 import views

urlpatterns =[
    path('custmorlist/', views.CustomerList.as_view()),
    path('custmorcreate/', views.CustomerCreate.as_view()),
    path('custmorretrieve/<int:pk>', views.CustomerRetrieve.as_view()),
    path('custmorupdate/<int:pk>', views.CustomerUpdate.as_view()),
    path('customerdestroy/<int:pk>', views.CustomerDestroy.as_view()),
    path('custmorlistcreate/<int:pk>', views.CustomerListCreate.as_view()),
    path('customerretrieveupdate/<int:pk>', views.CustomerRetrieveUpdate.as_view()),
    path('customerretrivedestroy/<int:pk>', views.CustomerRetrieveDestroy.as_view()),
    path('custmerretrieveupdatedestroy/<int:pk>', views.CustomerRetrieveUpdateDestroy.as_view()),

]