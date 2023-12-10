from django.contrib import admin
from django.urls import path, include
from menu.views import IndexPageView

app_name = 'menu'

urlpatterns = [
    path('menu/', IndexPageView.as_view(), name='index'),
    path('menu/<slug:menu>/<int:item>', IndexPageView.as_view(), name='menu')
]
