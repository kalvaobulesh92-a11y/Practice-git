from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('done/<int:pk>/',done,name="done"),
    path('edit/<int:pk>/',edit_task,name="edit_task"),
]