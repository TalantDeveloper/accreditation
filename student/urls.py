from django.urls import path

from student import views

app_name = 'student'

urlpatterns = [
    path('', views.students_view, name='students'),
    path('<int:student_id>/', views.student_view, name='student'),

    path('groups/', views.groups_view, name='groups'),
    path('groups/<int:group_id>/', views.group_view, name='group'),
]
