from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'product'

urlpatterns = [
    path("<str:category_name>/", views.CategoryView, name="category"),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    path('detail/<int:pk>/order', views.order, name='order'),

    path('product/agreement/', views.AgreementView.as_view(), name='agreement'),
    path('product/order/', views.RegisterView.as_view(), name='order'),
    path('product/csorder/', views.CsRegisterView.as_view(), name='csorder'),
    path('product/registerauth/', views.register_success, name='register_success'),
    path('product/activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
]
