from django.conf import settings
from django.db import transaction
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .decorators import login_message_required, admin_required, logout_message_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, FormView, TemplateView
from django.views.generic import View
from django.contrib.auth.views import PasswordResetConfirmView
from .forms import CsRegisterForm, RegisterForm
from .models import Product, Category, Order
from users.models import User
from .forms import CsRegisterForm, RegisterForm
from django.http import HttpResponse
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from .helper import send_mail, email_auth_num
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect, Http404
from django.forms.utils import ErrorList
from django.views.decorators.http import require_GET, require_POST
from django.core.exceptions import PermissionDenied

from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import PermissionDenied, ValidationError
from datetime import datetime
from django.views.generic import DetailView


def CategoryView(request, category_name):
    category_list = Product.objects.filter(category__category=category_name)
    categories = Category.objects.all()

    return render(
        request,
        "product/product_list.html",
        {
            "category_name" : category_name,
            "category_list" : category_list,
        }
    )

class ProductDetailView(DetailView):
    model = Product

def detail(request, id):
    product = Product.objects.get(id = id)
    product = get_object_or_404(Product, id=id)
    return render(request, 'product/product_detail.html', {'product' : product})

def order(request, id):
    product = Product.objects.get(id = id)
    product = get_object_or_404(Product, id=id)
    return render(request, 'product/product_order.html', {'product' : product})


# 회원가입 약관동의
@method_decorator(login_message_required, name='dispatch')
class AgreementView(View):
    def get(self, request, *args, **kwargs):
        request.session['agreement'] = False
        return render(request, 'product/agreement.html')

    def post(self, request, *args, **kwarg):
        if request.POST.get('agreement1', False) and request.POST.get('agreement2', False):
            request.session['agreement'] = True
            if request.POST.get('csregister') == 'csregister':
                return redirect('/product/product/csorder/')
            else:
                return redirect('/product/product/order/')
        else:
            messages.info(request, "약관에 모두 동의해주세요.")
            return render(request, 'product/agreement.html')


# 회원가입 인증메일 발송 안내 창
def register_success(request):
    if not request.session.get('register_auth', False):
        raise PermissionDenied
    request.session['register_auth'] = False

    return render(request, 'product/register_success.html')


# 회원가입
class CsRegisterView(CreateView):
    model = Order
    template_name = 'product/register_cs.html'
    form_class = CsRegisterForm

    def get(self, request, *args, **kwargs):
        if not request.session.get('agreement', False):
            raise PermissionDenied
        request.session['agreement'] = False

        url = settings.LOGIN_URL
        if request.user.is_anonymous:
            return HttpResponseRedirect('users:login')
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        # messages.success(self.request, "회원가입 성공.")
        self.request.session['register_auth'] = True
        messages.success(self.request, '회원님의 입력한 Email 주소로 인증 메일이 발송되었습니다. 인증 후 결제가 완료됩니다.')
        # return settings.LOGIN_URL
        return reverse('product:register_success')

    def form_valid(self, form):
        self.object = form.save()

        # 회원가입 인증 메일 발송
        # ISSUE - https 통신오류 -> http 프로토콜 수정
        send_mail(
            '[두리번 DooRiBun] {}님의 결제 인증메일 입니다.'.format(self.object.user_id),
            [self.object.email],
            html=render_to_string('product/register_email.html', {
                'user': self.object,
                'uid': urlsafe_base64_encode(force_bytes(self.object.pk)).encode().decode(),
                'domain': self.request.META['HTTP_HOST'],
                'token': default_token_generator.make_token(self.object),
            }),
        )
        return redirect(self.get_success_url())


# 일반 회원가입
class RegisterView(CsRegisterView):
    template_name = 'product/register.html'
    form_class = RegisterForm


# 이메일 인증 활성화
def activate(request, uid64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uid64))
        current_user = Order.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Order.DoesNotExist, ValidationError):
        messages.error(request, '메일 인증이 완료 되었습니다. 결제가 완료되었습니다!')
        return redirect('users:main')

    if default_token_generator.check_token(current_user, token):
        current_user.is_authenticated = True
        current_user.save()

        messages.info(request, '메일 인증이 완료 되었습니다. 결제가 완료되었습니다!')
        return redirect('users:main')

    messages.error(request, '메일 인증이 완료 되었습니다. 결제가 완료되었습니다!')
    return redirect('users:main')
