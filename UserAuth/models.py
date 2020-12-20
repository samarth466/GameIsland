from django.db import models
from datetime import date
# import datetime
from django import forms
from UserAuth.validators import validate_isnumeric
from django.contrib.auth.password_validation import MinimumLengthValidator, UserAttributeSimilarityValidator, CommonPasswordValidator, NumericPasswordValidator
# from tournaments.models import Room
from UserAuth.fields import DateField

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=400)
    user_username = models.CharField(max_length=128, primary_key=True)
    user_email = models.EmailField(
        max_length=256, unique=True, primary_key=False)
    user_password = models.CharField(max_length=30, validators=[
                                     MinimumLengthValidator, UserAttributeSimilarityValidator, CommonPasswordValidator, NumericPasswordValidator])
    user_birth_date = DateField()
    logged_in = models.BooleanField(default=False)
    security_pin = models.CharField(max_length=20, blank=False, null=True, default=None, validators=[
                                    validate_isnumeric], unique=True)
#    room = models.ForeignKey(
#        Room, on_delete = models.PROTECT, related_name = 'members', null = True, blank = True, default = None)

    def __str__(self):
        s = "You are signed in as {}"
        return s.format(self.user_email)

    class Meta:
        db_table = "User"
