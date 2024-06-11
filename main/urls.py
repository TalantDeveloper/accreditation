from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome, name='welcome'),

    path('tests/', views.result_tests_view, name='tests'),
    path('test/<int:student_id>/', views.result_test_view, name='test'),

    path('exam/', views.exam_view, name='exam')

]
