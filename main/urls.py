from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('login/', views.login_view, name='login'),

    path('tests/', views.result_tests_view, name='tests'),
    # path('test/', views.result_test_view, name='test'),

    path('exam/', views.exam_view, name='exam'),
    path('check/', views.check_exam, name='check'),

    path('results/', views.result_view, name='results'),
    path('result/<int:group_id>/', views.result_group, name='result'),

    path('create/', views.create_student, name='create'),

]
