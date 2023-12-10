from django.urls import path
from menu.views import IndexPageView

app_name = 'menu'

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('<slug:menu>/<path:item>', IndexPageView.as_view(), name='menu')  # May be int, slug
]
