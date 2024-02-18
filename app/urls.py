from django.urls import path
from . import views

urlpatterns = [
    path('user/signup/', views.signup, name="signup"),
    path('user/<int:id>/update/', views.update_profile, name="update_profile"),
    path('user/<int:id>', views.get_user_profile_by_id, name="get_user_profile_by_id"),
    path(
        'user/<str:username>/',
        views.get_user_profile_by_username,
        name="get_user_profile_by_username",
    ),
    path('user/<int:id>/delete/', views.delete_user, name="delete_user"),
]
