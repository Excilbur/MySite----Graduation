from django import forms
from django.contrib import auth
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=30, min_length=2,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    password = forms.CharField(label='密码', min_length=6,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))
    password_again = forms.CharField(label='再输入一次密码', min_length=6,
                                     widget=forms.PasswordInput(
                                         attrs={'class': 'form-control', 'placeholder': '请再输入密码'}))
    email = forms.EmailField(label='邮箱',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '请输入邮箱'}))

    #验证用户名
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在')
        return username
    #验证邮箱
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱已存在')
        return email
    # 验证密码两次是否一致
    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('两次输入密码不一致')
        return password_again

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '请输入密码'}))

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        #验证用户名密码
        user = auth.authenticate(username=username, password=password)
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        else:
            self.cleaned_data['user'] = user
        return self.cleaned_data


