from django import forms
from django.contrib.auth.hashers import check_password
from .models import Order
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, SetPasswordForm, UserCreationForm, \
    PasswordChangeForm
from django.contrib.auth import get_user_model
from .choice import *


def hp_validator(value):
    if len(str(value)) != 10:
        raise forms.ValidationError('정확한 핸드폰 번호를 입력해주세요.')


# 컴공 회원가입 폼
class CsRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CsRegisterForm, self).__init__(*args, **kwargs)

        self.fields['user_id'].label = '아이디'
        self.fields['user_id'].widget.attrs.update({
            # 'class': 'form-control col-sm-10',
            'class': 'form-control',
            # 'placeholder': '아이디를 입력해주세요.',
            'autofocus': False
        })
        self.fields['password1'].label = '비밀번호'
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': '비밀번호를 입력해주세요.',
        })
        self.fields['password2'].label = '비밀번호 확인'
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': '비밀번호를 다시 입력해주세요.',
        })
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': '회원가입 후 입력하신 메일로 본인인증 메일이 전송됩니다.',
        })
        self.fields['name'].label = '이름'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': "아이디, 비밀번호 찾기에 이용됩니다.",
        })
        self.fields['hp'].label = '핸드폰번호'
        self.fields['hp'].validators = [hp_validator]
        self.fields['hp'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': "'-'를 제외한 숫자로 입력해주세요",
        })
        self.fields['grade'].label = '국적'
        self.fields['grade'].widget.attrs.update({
            'class': 'form-control',
        })

    class Meta:
        model = Order
        fields = ['user_id', 'password1', 'password2', 'email', 'name', 'hp', 'grade']

    def save(self, commit=True):
        order = super(CsRegisterForm, self).save(commit=False)
        order.level = '2'
        order.is_active = False
        order.save()

        return order


# 일반 회원가입 폼
class RegisterForm(UserCreationForm):
    grade = forms.ChoiceField(choices=COUNT_CHOICES, label='인원', widget=forms.Select(
        attrs={'class': 'form-control'}),
                              )

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        self.fields['user_id'].label = '아이디'
        self.fields['user_id'].widget.attrs.update({
            # 'class': 'form-control col-sm-10',
            'class': 'form-control',
            'autofocus': False,
            # 'placeholder': '아이디를 입력해주세요.',
        })
        self.fields['password1'].label = '비밀번호'
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': '비밀번호를 입력해주세요.',
        })
        self.fields['password2'].label = '비밀번호 확인'
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': '비밀번호를 다시 입력해주세요.',
        })
        self.fields['email'].label = '이메일'
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': '회원가입 후 입력하신 메일로 본인인증 메일이 전송됩니다.',
        })
        self.fields['name'].label = '이름'
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': "아이디, 비밀번호 찾기에 이용됩니다.",
        })
        self.fields['hp'].label = '핸드폰번호'
        self.fields['hp'].validators = [hp_validator]
        self.fields['hp'].widget.attrs.update({
            'class': 'form-control',
            # 'placeholder': "'-'를 제외한 숫자로 입력해주세요",
        })

    class Meta:
        model = Order
        fields = ['user_id', 'password1', 'password2', 'email', 'name', 'hp', 'grade']

    def save(self, commit=True):
        order = super(RegisterForm, self).save(commit=False)
        order.level = '3'
        order.is_active = False
        order.save()

        return order
