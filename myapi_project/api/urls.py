from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student-list'),
    path('students/create/', views.student_create, name='student-create'),
    path('students/<int:pk>/', views.student_detail, name='student-detail'),
    path('students/<int:pk>/update/', views.student_update, name='student-update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student-delete'),
]
