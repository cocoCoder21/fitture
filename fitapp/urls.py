from django.urls import path
from fitapp import views

app_name = 'fitapp'

urlpatterns = [
    path('', views.home, name='user-account'),
    path('dashboard/', views.user_login, name='dash'),
    path('settings/', views.settings, name='settings'),
]
