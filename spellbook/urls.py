from . import views
from django.urls import path

urlpatterns = [
    path('', views.SpellList.as_view(), name='home'),
    path('spell/<int:id>/', views.spell_detail, name='spell_detail'),
    path('spell/create', views.spell_create, name='spell_create'),
    path('spell/edit/<int:id>/', views.spell_edit, name='spell_edit'),
    path('spell/delete/<int:id>/', views.spell_delete, name='spell_delete'),
    path('about', views.spell_about, name='spell_about')
]
