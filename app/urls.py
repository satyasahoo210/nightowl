from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('change_password', views.change_password, name='change_password'),
    path('profile/edit', views.profile_edit, name='profile_edit'),

    path('dp/<username>', views.profile_picture, name='profile_picture'),
    path('profile/<username>', views.profile, name='profile'),
    
    path('<type>/<pk>', views.establishment, name='establishment'),
]
