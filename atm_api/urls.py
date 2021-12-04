from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from atm_api import views

urlpatterns = [
    url(r'^atm/withdrawl$', views.withdrawl),
    url(r'^admin/currency/$', views.add_currency),
]
