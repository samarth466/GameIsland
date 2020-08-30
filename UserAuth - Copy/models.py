from django.db import models
from datetime import date
import datetime
from django import forms
from UserAuth.validators import validate_isnumeric
from django.contrib.auth.password_validation import MinimumLengthValidator, UserAttributeSimilarityValidator, CommonPasswordValidator, NumericPasswordValidator

# Create your models here.

class DateField(models.Field):

    def __init__(self,date=None, default=datetime.date(date.today().year,1,1), *args, **kwargs):
        self.date = date
        if self.date == None:
            self.date = kwargs['default'] = datetime.datetime(default.year,default.month,default.day)
        kwargs['unique'] = False
        kwargs['blank'] = False
        kwargs['null'] = True
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        if self.date != None:
            kwargs['date'] = self.date
        return name, path, args, kwargs

    def pre_save(self, model_instance, add):
        value = self.date
        setattr(model_instance,self.attname,value)
        return value

    def db_type(self, connection):
        return 'Date'

    def formfield(self, **kwargs):
        defaults = {'form_class':forms.DateField}
        defaults.update(kwargs)
        return super().formfield(**defaults)

class User(models.Model):
    user_name = models.CharField(max_length=400)
    user_username = models.CharField(max_length=128,primary_key=True)
    user_email = models.EmailField(max_length=256,unique=True,primary_key=False)
    user_password = models.CharField(max_length=30,validators=[MinimumLengthValidator,UserAttributeSimilarityValidator,CommonPasswordValidator,NumericPasswordValidator])
    user_birth_date = DateField()
    logged_in = models.BooleanField(default=False)
    security_pin = models.CharField(max_length=20,blank=False,null=True,default=None,validators=[validate_isnumeric],unique=True)

    def __str__(self):
        s = "You are signed in as {}"
        return s.format(self.user_email)

    class Meta:
        db_table = "User"