from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import UserModel


class UserCreationForm(forms.ModelForm):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput)
    last_name = forms.CharField(label="Last Name", widget=forms.TextInput)
    username = forms.CharField(label="User Name", widget=forms.TextInput)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ('email', 'first_name', 'username')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = UserModel
        fields = ('email', 'password', 'first_name', 'last_name', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]
