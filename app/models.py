from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    AbstractUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.validators import validate_email


class UserProfileManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **kwargs)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **kwargs)


# Custom User
class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=[ASCIIUsernameValidator()],
    )
    email = models.EmailField(unique=True, validators=[validate_email])
    budget_goal = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    expected_income_per_annum = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.0, null=True
    )
    date_of_birth = models.DateField(null=True, blank=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
    EMAIL_FIELD = "email"
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()


class Category(models.Model):
    GROCERIES = "Groceries"
    ENTERTAINMENT = "Entertainment"
    EDUCATION = "Education"
    HEALTHCARE = "Healthcare"
    TRAVEL = "Travel"
    UTILITIES = "Utilities"
    OTHER = "Other"

    CATEGORY_CHOICES = (
        (GROCERIES, "Groceries"),
        (ENTERTAINMENT, "Entertainment"),
        (EDUCATION, "Education"),
        (HEALTHCARE, "Healthcare"),
        (TRAVEL, "Travel"),
        (UTILITIES, "Utilities"),
        (OTHER, "Other"),
    )

    name = models.CharField(unique=True, max_length=255, choices=CATEGORY_CHOICES)


class Expense(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    remarks = models.TextField(null=True)
