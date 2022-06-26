from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.player),
    path('<int:pk>', views.game, name='game')
    ]