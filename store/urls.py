from django.urls import path
from store import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('reg',views.final_reg,name='reg'),
    path('log',views.final_log,name='log'),
    ]
