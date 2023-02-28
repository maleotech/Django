from django.urls import path
from .views import StudentCreateView, StudentDetailView, StudentListView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]

    # path('', views.student_list, name='student_list'),
    # path('student/<int:pk>/', views.student_detail, name='student_detail'),
    # path('student/create/', views.student_create, name='student_create'),
    # path('student/update/<int:pk>/', views.student_update, name='student_update'),