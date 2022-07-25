from django.urls import path
from logs import views

urlpatterns = [
    path("logs/", views.log_list),
    path("logs/<int:pk>/", views.log_detail),
]
