from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError

from accounts.models import UserLink


class UserCreationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})
        self.fields['password_confirm'].widget.attrs.update({'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})

    username = forms.CharField(max_length=50, label='Username', required=True)
    password = forms.CharField(max_length=100, label='Password:', strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, label='Confirm password:', widget=forms.PasswordInput, strip=False)
    first_name = forms.CharField(label='First name:', max_length=100, required=False)
    last_name = forms.CharField(label='Last name:', max_length=100, required=False)
    email = forms.CharField(label='Email:', required=True)

    def clean_username(self):
        username = self.cleaned_data.get('username')
        try:
            User.objects.get(username=username)
            raise ValidationError('User with this username already exists!',
                                  code='user_username_exists')
        except User.DoesNotExist:
            return username

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')

        if not (first_name or last_name):
            raise forms.ValidationError('First name or last name needs to fill out!')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        try:
            User.objects.get(email=email)
            raise ValidationError('User with this email already exists!',
                                  code='user_email_exists')
        except User.DoesNotExist:
            return email

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Password does not matches!')
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']


# class UserUpdateForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email')
#         labels = {'first_name': 'First name', 'last_name': 'Last name', 'email': 'Email'}

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserLink
        fields = ['link']



class UserLinkForm(forms.ModelForm):
    class Meta:
        model = UserLink
        fields = ['link']


class UserUpdatePasswordForm(forms.ModelForm):
    password = forms.CharField(max_length=100, label='New Password:', strip=False,
                               widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=100, label='New Password Confirm:',
                                       widget=forms.PasswordInput, strip=False)
    old_password = forms.CharField(max_length=100, label='Old Password:',
                               widget=forms.PasswordInput)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user = self.instance
        if not user.check_password(old_password):
            raise ValidationError('Invalid old password', code='invalid_password')
        return old_password

    def clean_password_confirm(self):
        super().clean()
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError('New password does not matches!')
        return password_confirm

    def save(self, commit=True):
        user = self.instance
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['password', 'password_confirm', 'old_password']