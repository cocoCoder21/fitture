from django.urls import path
from fitapp import views

app_name = 'fitapp'

urlpatterns = [
    path('', views.home, name='user-account'),
    path('dashboard/', views.dashboard, name='dash'),
    path('settings/', views.settings, name='settings'),
    path('user_profile/<str:username>', views.user_page, name='user_profile')
]
