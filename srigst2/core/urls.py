from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('founders/', views.founders, name='founders'),
    path('contact/', views.contact, name='contact'),
    path('enquiry/', views.enquiry, name='enquiry'),
    path('manager/login/', views.manager_login, name='manager_login'),
    path('manager/logout/', views.manager_logout, name='manager_logout'),
    path('manager/upload/', views.manager_upload, name='manager_upload'),
    path('manager/photos/', views.manager_photos, name='manager_photos'),
    path('manager/delete/', views.manager_delete, name='manager_delete'),
    path('manager/review/', views.manager_review, name='manager_review'),
]
