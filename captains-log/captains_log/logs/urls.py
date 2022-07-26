from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from logs import views

urlpatterns = [
    path("logs/", views.log_list),
    path("logs/<int:pk>/", views.log_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
