from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.core.validators import validate_email


# Custom User
class UserProfile(AbstractBaseUser):
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
    date_of_birth = models.DateField(null=True)
    USERNAME_FIELD = "username"


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
