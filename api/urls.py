from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('Todo-list/', views.TodoList, name="Todo-list"),
	path('Todo-detail/<str:pk>/', views.TodoDetail, name="Todo-detail"),
	path('Todo-create/', views.TodoCreate, name="Todo-create"),

	path('Todo-update/<str:pk>/', views.TodoUpdate, name="Todo-update"),
	path('Todo-delete/<str:pk>/', views.TodoDelete, name="Todo-delete"),
]
