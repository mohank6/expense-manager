from app.models import UserProfile
from django.db.models import Q


def create_user(data):
    user = UserProfile(**data)
    try:
        user.set_password(data.get('password'))
        user.full_clean()
        user.save()
        return user
    except Exception as e:
        raise e


def get_user_by_username(username):
    user = UserProfile.objects.filter(username=username).first()
    return user


def get_user_by_email(email):
    user = UserProfile.objects.filter(email=email).first()
    return user


def get_user_by_id(id):
    user = UserProfile.objects.filter(id=id).first()
    return user


def get_user_by_username_or_email(username, email):
    user = UserProfile.objects.filter(Q(username=username) | Q(email=email)).first()
    return user


def update_user(data, id):
    user = get_user_by_id(id=id)
    for key, value in data.items():
        setattr(user, key, value)
    try:
        user.full_clean()
        user.save()
        return user
    except Exception as e:
        raise e


def delete_user(id):
    user = get_user_by_id(id=id)
    user.delete()
