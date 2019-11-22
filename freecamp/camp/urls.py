from . import views
from django.urls import path,include
from django.conf.urls import url


urlpatterns = [
path('doc_login/',views.doc_login,name='doc_login'),
path('org_login/',views.org_login,name='org_login'),
path('doc_sign/',views.doc_sign,name='doc_sign'),
path('org_sign/',views.org_sign,name='org_sign'),
path('register/',views.register,name = 'register'),
path('doc_logged/',views.doc_logged,name = 'doc_logged'),
path('org_logged/',views.org_logged,name='org_logged'),
path('nregister/',views.nregister,name='nregister'),
path('doc_signed/',views.doc_signed,name='doc_signed'),
path('org_signed/',views.org_signed,name='org_signed'),
]