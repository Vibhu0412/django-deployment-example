from django.urls import path
from basic_app import views

#FOR TEMPLATE TAGGINg to use in HTML filesssss
# GLOBALNAME = APPLICATION NAME

app_name = 'basic_first_app'
#define namespace in project/url.py
urlpatterns = [
    path('relative/',views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
