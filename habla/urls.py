from django.urls import path
from . import views
#URLConf
urlpatterns = [
    path('', views.home, name = 'home'),
    path('send_sessage/', views.send_message, name='send_message'),
]