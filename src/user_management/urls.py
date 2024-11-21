from django.urls import path
from . import views


urlpatterns = [
    # Utilisateurs
    path('users/', views.list_users, name='list-users'),
    path('users/create/', views.create_user, name='create-user'),
    path('users/<int:user_id>/update/', views.update_user, name='update-user'),
    path('users/<int:user_id>/delete/', views.delete_user, name='delete-user'),

    # Sous-profils
    path('subprofiles/', views.list_sub_profiles, name='list-sub-profiles'),
    path('subprofiles/create/', views.create_sub_profile, name='create-sub-profile'),
    path('subprofiles/<int:subprofile_id>/update/', views.update_sub_profile, name='update-sub-profile'),
    path('subprofiles/<int:subprofile_id>/delete/', views.delete_sub_profile, name='delete-sub-profile'),
]