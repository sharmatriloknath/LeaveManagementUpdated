from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import LeaveBalance, LeavesRequest


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user


def create_user_account(email, password, first_name="",
                        last_name="", **extra_fields):
    user = get_user_model().objects.create_user(
        email=email, password=password, first_name=first_name,
        last_name=last_name, **extra_fields)
    return user


def leave_approval(requested_days, user_id, leave_type):
    balance = LeaveBalance.objects.filter(user_id=user_id, leave_type=leave_type)
    user = get_user_model().objects.filter(user_id=user_id)
    if user.role == 'Manager' or 'hr':
        available_days = user.available_days
        if available_days > requested_days:
            available_days = available_days - requested_days
            balance.available_days = available_days
            LeavesRequest.objects.create(requested_days=requested_days, from_date=from_date, to_date=to_date, state='approved', leave_type=leave_type, user=user_id)
        else:
            raise serializers.ValidationError("You Don't Have Enough Balance For This Type Of Leave")