from django import forms
from UserAuth.models import User
from UserAuth.validators import validate_isnumeric
import datetime
from django.contrib.auth.password_validation import MinimumLengthValidator, UserAttributeSimilarityValidator, NumericPasswordValidator
<<<<<<< HEAD
from UserAuth.widgets import DateInput
from django.forms import ModelForm
=======
from bootstrap_datepicker_plus import DatePickerInput
>>>>>>> 79371c4de2ebd9fb67cf9053c7b4d3ef0ead4848

# Create the form class.

class RegistrationForm(forms.Form):
    email = forms.EmailField()
    email.max_length = 256
    email.min_length = 8
    email.strip = True
    email.label = "Enter your email address"

class LogInForm(forms.Form):
    email = forms.EmailField()
    email.max_length = 256
    email.min_length = 8
    email.strip = True
    email.label = "Enter your email address"
    password = forms.CharField(label = "Enter your password", widget = forms.PasswordInput)
    password.max_length = 30
    password.min_length = 8
    password.validators = [MinimumLengthValidator,UserAttributeSimilarityValidator]

class NewUserAccountForm(forms.Form):
    first_name = forms.CharField()
    first_name.max_length = 200
    first_name.min_length = 3
    first_name.label = "Enter your first name"
    last_name = forms.CharField()
    last_name.max_length = 200
    last_name.min_length = 3
    last_name.label = "Enter your last name"
    user_name = forms.CharField()
    user_name.max_length = 128
    user_name.min_length = 5
    user_name.label = "Enter your game name"
    now = datetime.datetime.now()
    YEARS = [x for x in range(now.year-100,now.year)]
<<<<<<< HEAD
    date_of_birth = forms.SelectDateWidget(years=YEARS)
=======
    date_of_birth1 = forms.DateField(label = "Enter your date of birth", widget=forms.SelectDateWidget(years=YEARS))
    date_of_birth2 = forms.DateField(label="Enter your date of birth ",widget=DatePickerInput(format='%m/%d/%Y'))
>>>>>>> 79371c4de2ebd9fb67cf9053c7b4d3ef0ead4848
    email = forms.EmailField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    email.label = "Enter your email address"
    password1 = forms.CharField(label = "Enter your password", min_length = 8, max_length = 30, widget = forms.PasswordInput)
    password1.validators = [UserAttributeSimilarityValidator,MinimumLengthValidator]
    password2 = forms.CharField(label = "Reenter your password for confirmation", min_length = 8, max_length = 30, widget = forms.PasswordInput)
    password2.validators = [MinimumLengthValidator,UserAttributeSimilarityValidator]

class ProfileForm(forms.Form):
    pin = forms.CharField(label="Enter your pin ",max_length=20,min_length=5,widget=forms.PasswordInput)
    pin.validators = [validate_isnumeric]
