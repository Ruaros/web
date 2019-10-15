from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('',                home),
    path('home/',           home,               name='home_url'),
    path('contacts/',       contacts,           name='contacts_url'),
    path('services/',       services,           name='services_url'),
    path('building/',       building,           name='building_url'),
    path('design/',         design,             name='design_url'),
    path('feedback/',       make_Contact.as_view(), name='feedback_url'), 
    path('done_projects/',  done_projects,      name='done_projects_url'),
    path('houses/',         houses,             name='houses_url'),
    path('complexes/',      complexes,          name='complexes_url'),
    path('hotels/',         hotels,             name='hotels_url'),
    path('ets/',            ets,                name='ets_url'),
    path('expertise/',      expertise,          name='expertise_url'),
    path('create/',         project_create.as_view(),     name='create_project_url'),
    path(r'<str:type>/filter/',    filtrate,           name='filtrate_url'),
    path(r'<str:type>/<str:article>/',   project_page,    name='project_page_url'),
    path(r'<str:type>/<str:article>/update/',   project_update.as_view(), name='update_project_url'),
    path(r'<str:type>/<str:article>/delete/',   project_delete.as_view(), name='delete_project_url'),
    
]  

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    #urlpatterns = [
    #    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    #    url(r'', include('django.contrib.staticfiles.urls')),
    #
    #    # --- error pages ---
    #    url(r'^403$', handler403),
    #    url(r'^404$', handler404),
    #    url(r'^500$', handler500),
    #] + urlpatterns