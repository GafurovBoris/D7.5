from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail
from django.core.mail import mail_managers


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    first_name = forms.CharField(label="Имя")
    last_name = forms.CharField(label="Фамилия")

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        authors = Group.objects.get(name="authors")
        user.groups.add(authors)
        return user

class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        common_users = Group.objects.get(name="common users")
        user.groups.add(common_users)

        send_mail(
            subject='Welcome to our News Portal!',
            message=f'{user.username}, you have successfully registered!',
            from_email=None,  # будет использовано значение DEFAULT_FROM_EMAIL
            recipient_list=[user.email],)

        return user