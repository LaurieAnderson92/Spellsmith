from . import views
from django.urls import path

urlpatterns = [
    path('', views.SpellList.as_view(), name='home'),
]