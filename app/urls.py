from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),

    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),

    path('change_password', views.change_password, name='change_password'),
    path('profile/edit', views.profile_edit, name='profile_edit'),

    path('establishment/new', views.EstablishmentCreateView.as_view(), name='establishment.new'),
    path('establishment/<pk>/update', views.EstablishmentUpdateView.as_view(), name='establishment.update'),

    path('dp/<username>', views.profile_picture, name='profile_picture'),
    path('profile/<username>', views.profile, name='profile'),
    
    path('<type>/<pk>', views.establishment, name='establishment'),
    path('<type>/<pk>/delete', views.EstablishmentDeleteView.as_view(), name='establishment.delete'),
    
    path('review/<pk>/new', views.ReviewCreateView.as_view(), name='review.new'),
    path('image/<pk>/new', views.AddPhotoView.as_view(), name='photo.new'),

    path('<type>/<pk>/image/<id>', views.estd_image, name='estd_image'),
]
