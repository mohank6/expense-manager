from datetime import datetime
from . import expense_accessor
from django.forms.models import model_to_dict
from ..user import user_accessor


def get_expense_data(expense):
    expense_data = model_to_dict(
        expense,
        fields=[
            'id',
            'user',
            'amount',
            'date',
            'category',
            'remarks',
        ],
    )
    expense_data['category_name'] = expense.category.name
    return expense_data


def handle_get_expense(id):
    expense = expense_accessor.get_expense_by_id(id)
    if not expense:
        return ({'message': f'Expense with id:{id} doesnot exists.'}, 404)
    return (get_expense_data(expense), 200)


def handle_get_expenses_by_user(id):
    user = user_accessor.get_user_by_id(id=id)
    if not user:
        return ({'message': f'User doesnot exists.'}, 404)
    expenses = expense_accessor.get_all_expenses_of_user(user=user)
    if not expenses:
        return ({'message': f'User has no expenses'}, 404)
    return ([get_expense_data(expense) for expense in expenses], 200)


def handle_get_total_amount_spent_by_user(id):
    user = user_accessor.get_user_by_id(id=id)
    if not user:
        return ({'message': f'User doesnot exists.'}, 404)
    amount_spent = expense_accessor.get_total_expenses(user=user)
    return ({'total_amount_spent': amount_spent}, 200)


def handle_create_expense(data):
    validated_data = validate_create_expense(data)
    if not validated_data:
        return ({'message': 'Validation error'}, 400)
    expense = expense_accessor.create_expense(validated_data)
    return (get_expense_data(expense=expense), 201)


def handle_update_expense(data, id):
    expense = expense_accessor.get_expense_by_id(id)
    if not expense:
        return ({'message': f'Expense not found.'}, 400)
    validated_data = validate_update_expense(data)
    if not validated_data:
        return ({'message': 'Validation error'}, 400)
    expense = expense_accessor.update_expense(id, validated_data)
    return (get_expense_data(expense=expense), 201)


def handle_delete_expense(id):
    expense = expense_accessor.get_expense_by_id(id)
    if not expense:
        return ({'message': f'Expense not found.'}, 400)
    expense_accessor.delete_expense(id=id)
    return ({'message': 'Expense deleted'}, 204)


def validate_data(data, required_fields, optional_fields):
    validated_data = {}
    for required_field in required_fields:
        if required_field not in data.keys():
            return False
        validated_data[required_field] = data[required_field]
    for opt_field in optional_fields:
        try:
            validated_data[opt_field] = data[opt_field]
        except:
            pass
    return validated_data


def validate_create_expense(data):
    required_fields = ['user', 'amount', 'date', 'category']
    optional_fields = ['remarks']
    validated_data = validate_data(data, required_fields, optional_fields)
    if not validated_data:
        return False
    category = expense_accessor.get_category_by_id(validated_data.get('category'))
    if not category:
        return False
    validated_data['category'] = category
    user = user_accessor.get_user_by_id(validated_data['user'])
    if not user:
        return False
    validated_data['user'] = user
    try:
        formatted_date = datetime.strptime(validated_data['date'], '%Y-%m-%d')
    except:
        return False
    validated_data['date'] = formatted_date
    return validated_data


def validate_update_expense(data):
    required_fields = []
    optional_fields = [
        'remarks',
        'amount',
        'date',
    ]
    validated_data = validate_data(data, required_fields, optional_fields)
    if not validated_data:
        return False
    try:
        formatted_date = datetime.strptime(validated_data['date'], '%Y-%m-%d')
    except:
        return False
    validated_data['date'] = formatted_date
    return validated_data
