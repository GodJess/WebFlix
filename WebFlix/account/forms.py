from django.forms import ModelForm, TextInput
from .models import UserData

class AddUser(ModelForm):
    class Meta:
        model = UserData
        fields = ["login", "name", "surname", "mail", 'password', 'image']

        widgets = {
            "login" : TextInput(attrs={
                "autocomplete": "off",
                "class": "input-login",
                "type": "text",
                "name": "login",
                "placeholder": "Логин*"
            }),
            "name" : TextInput(attrs={
                "autocomplete": "off",
                "class": "fname",
                "type": "text",
                "name": "fname",
                "placeholder": "Имя*"
            }),
            "surname": TextInput(attrs={
                "autocomplete": "off",
                "class": "fname",
                "type": "text",
                "name": "lname",
                "placeholder": "Фамилия*"
            }),
             "mail": TextInput(attrs={
                "autocomplete": "off",
                "class": "input-mail",
                "type": "text",
                "name": "mail",
                "placeholder": "Почта*"
            }),
            "password": TextInput(attrs={
                "autocomplete": "off",
                "class": "password",
                "type": "password",
                "name": "password",
                "placeholder": "Пароль*"
            }),
            "image": TextInput(attrs={
                "autocomplete": "off",
                "type": "hidden",
                "value": "none"
            }),
        }