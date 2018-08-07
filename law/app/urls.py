
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'/signup/admin/$', views.CreateAdmin,name='adminsignup'),
    url(r'/signup/user/$', views.CreateCustomer,name='customer'),

]
