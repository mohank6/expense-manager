from app.models import Expense, Category
from django.db.models import Sum


def create_expense(data):
    expense = Expense(**data)
    try:
        expense.full_clean()
        expense.save()
        return expense
    except Exception as e:
        return e


def get_expense_by_id(id):
    expense = Expense.objects.filter(id=id).first()
    return expense


def get_all_expenses_of_user(user):
    expenses = Expense.objects.filter(user=user).all()
    return expenses


def update_expense(id, data):
    expense = get_expense_by_id(id)
    for key, value in data.items():
        setattr(expense, key, value)
    try:
        expense.full_clean()
        expense.save()
        return expense
    except Exception as e:
        return e


def delete_expense(id):
    expense = get_expense_by_id(id)
    expense.delete()


def get_total_expenses(user):
    total_expenses = Expense.objects.filter(user=user).aggregate(total=Sum('amount'))
    return total_expenses['total'] or 0.0


def get_category_by_id(id):
    category = Category.objects.filter(id=id).first()
    return category


def get_all_categories(id):
    categories = Category.objects.all()
    return categories
