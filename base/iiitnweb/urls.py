from django.conf.urls import url

from . import views

urlpatterns = [
		url('', views.home, name='home'),
        url('', views.Admission.admission, name='admission'),
        url('', views.Admission.undergraduate, name='admission'),
]

