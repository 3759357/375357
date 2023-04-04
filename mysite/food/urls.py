from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='question_list'),
    path('<int:question_id>/', views.detail),

]