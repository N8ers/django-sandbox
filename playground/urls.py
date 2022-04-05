from django.urls import path
from . import views

# URLConf
urlpatterns = [
  path('hello_html/', views.say_hello_html),
  path('hello_template/', views.say_hello)
]