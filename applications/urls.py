from django.urls import path
from . import views

urlpatterns=[
    path('',views.user_input),
    path('name/',views.linked_jobs,name='linked_jobs'),
    path('saved/',views.save_company,name='save_company'),
]
