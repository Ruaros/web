"""
Definition of urls for Site.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.urls import include
from django.views.defaults import server_error, page_not_found, permission_denied

#handler403 = curry(permission_denied, template_name='errs/403.html')
#handler404 = curry(page_not_found, template_name='errs/404.html')
#handler500 = curry(server_error, template_name='errs/500.html')


urlpatterns = [
    #path('contact/', views.contact, name='contact'),
    #path('about/', views.about, name='about'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('adminkin/', admin.site.urls),
    path('', include('veb_site.urls')),
 
] 

