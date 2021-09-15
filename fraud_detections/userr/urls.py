from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_login, name='user_log'),
    path('log/', views.user_login, name='user_log'),
    path('user_registration/', views.user_registration, name='user_reg'),
    path('user_home/', views.user_home, name='user_home'),

    path('register/', views.registration),
    path('login/', views.login),
    path('submit/', views.credit_data_submit, name='submit'),
    path('inputvalues/<int:userid>',views.inputvalues,name='inputvalues'),
    # path('credit_data_submit',views.credit_data_submit,name='credit_data_submit')
]
