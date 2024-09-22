from . import views
from django.urls import path

urlpatterns = [
    path('', views.SpellList.as_view(), name='home'),
    path('<int:id>/', views.spell_detail, name='spell_detail'),
]