from django.urls import path
from store import views
from store.views.index import index 
from store.views.Signup import Signup
from store.views.Signin import Signin
from  store.views.forgot import forgot

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',Signup.as_view(),name='signup'),
    path('signin',Signin.as_view(),name='signin'),
    path('forgot',forgot.as_view(),name='forgot'),
    # path('reg',views.final_reg,name='reg'),
    # path('log',views.final_log,name='log'),
    ]
