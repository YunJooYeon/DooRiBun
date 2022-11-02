from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'product'

urlpatterns = [
    #url(r'^(?P<category_id>[0-9]+)/$', views.CategoryView, name='category'),
   path("<str:category_name>/", views.CategoryView, name="category"),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
 path('detail/<int:pk>/order', views.order, name='order'),

 #path("/<int:pk>/", views.CategoryView, name="category"),

    # path('', views.index),
    # # path('login/', views.login_view, name='login'),
    # path('product/main/', views.main_view, name='main'),
    # path('product/login/', views.LoginView.as_view(), name='login'),
    # path('product/logout/', views.logout_view, name='logout'),
    #
    # path('product/recovery/id/', views.RecoveryIdView.as_view(), name='recovery_id'),
    # path('product/recovery/pw/', views.RecoveryPwView.as_view(), name='recovery_pw'),
    # path('product/recovery/id/find/', views.ajax_find_id_view, name='ajax_id'),
    # path('product/recovery/pw/find/', views.ajax_find_pw_view, name='ajax_pw'),
    # path('product/recovery/pw/auth/', views.auth_confirm_view, name='recovery_auth'),
    # path('product/recovery/pw/reset/', views.auth_pw_reset_view, name='recovery_pw_reset'),
    # # path('recovery/reset/', views.AuthPwResetView.as_view(), name='recovery_pw_reset'),

    path('product/agreement/', views.AgreementView.as_view(), name='agreement'),
    # path('register/', views.register_view, name='register'),
    path('product/order/', views.RegisterView.as_view(), name='order'),
    # path('csregister/', views.cs_register_view, name='csregister'),
    path('product/csorder/', views.CsRegisterView.as_view(), name='csorder'),
    path('product/registerauth/', views.register_success, name='register_success'),
    path('product/activate/<str:uid64>/<str:token>/', views.activate, name='activate'),
    #
    # path('product/profile/', views.profile_view, name='profile'),
    # path('product/profile/post', views.profile_post_view, name='profile_post'),
    # path('product/profile/comment', views.profile_comment_view, name='profile_comment'),
    # path('product/profile/update/', views.profile_update_view, name='profile_update'),
    # path('product/profile/delete/', views.profile_delete_view, name='profile_delete'),
    # path('product/profile/password/', views.password_edit_view, name='password_edit'),
]
