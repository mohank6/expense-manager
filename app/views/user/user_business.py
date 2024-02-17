from . import user_accessor
from django.forms.models import model_to_dict
import json


def get_user_data(user):
    user_data = model_to_dict(
        user,
        fields=[
            'id',
            'username',
            'email',
            'budget_goal',
            'date_of_birth',
            'expected_income_per_annum',
        ],
    )
    return user_data


def handle_signup(data):
    validated_data = validate_user_create(data)
    if not validated_data:
        return ({'message': 'Validation error'}, 400)
    try:
        user = user_accessor.create_user(data=validated_data)
        return (get_user_data(user), 201)
    except Exception as e:
        return ({'error': str(e)}, 400)


def handle_update(data, id):
    validated_data = validate_user_update(data)
    if not validated_data:
        return ({'message': 'Validation error'}, 400)
    user = user_accessor.get_user_by_id(id)
    if not user:
        return ({'message': 'User doesnot exists.'}, 400)
    try:
        user = user_accessor.update_user(data=validated_data, id=id)
        return (get_user_data(user), 201)
    except Exception as e:
        return ({'error': str(e)}, 400)


def handle_get_user(id=None, email=None, username=None):
    if id:
        user = user_accessor.get_user_by_id(id=id)
    if username:
        user = user_accessor.get_user_by_username(username=username)
    if email:
        user = user_accessor.get_user_by_email(email=email)
    if not user:
        return ({'message': 'User not found'}, 404)
    return (get_user_data(user), 200)


def handle_delete(id):
    user = user_accessor.get_user_by_id(id=id)
    if not user:
        return ({'message': 'User doesnot exists'}, 400)
    user_accessor.delete_user(id=id)
    return ({'message': 'User deleted'}, 204)


def validate_user_create(data):
    required_fields = ['username', 'email', 'budget_goal', 'password']
    optional_fields = ['date_of_birth', 'expected_income_per_annum']
    return validate_data(data, required_fields, optional_fields)


def validate_user_update(data):
    required_fields = []
    optional_fields = ['budget_goal', 'date_of_birth', 'expected_income_per_annum']
    return validate_data(data, required_fields, optional_fields)


def validate_data(data, required_fields, optional_fields):
    validated_data = {}
    data_keys = data.keys()
    for field in required_fields:
        if field not in data_keys:
            return False
        validated_data[field] = data[field]
    for opt_field in optional_fields:
        try:
            validated_data[opt_field] = data[opt_field]
        except:
            pass
    return validated_data
