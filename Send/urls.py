from django.urls import path,include
from django.conf.urls import url
from Send import views
urlpatterns = [
    path('', views.sent,name="Send"),
]
