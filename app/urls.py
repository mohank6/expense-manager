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
    path('expense/create/', views.create_expense, name="create_expense"),
    path('expense/<int:id>', views.get_expense_by_id, name="get_expense_by_id"),
    path(
        'expense/user/<int:id>', views.get_expenses_by_user, name="get_expenses_by_user"
    ),
    path('expense/<int:id>/update/', views.update_expense, name="update_expense"),
    path(
        'expense/user/<int:id>/total/',
        views.get_total_amount_spent_by_user,
        name="get_total_amount_spent_by_user",
    ),
    path('expense/<int:id>/delete/', views.delete_expense, name="delete_expense"),
]
