from django.urls import path

from todo import views

urlpatterns = [
    path("", views.TodoListView.as_view(), name="todo"),
]
