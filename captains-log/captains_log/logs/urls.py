from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from logs import views

urlpatterns = [
    path("logs/function", views.log_list),  # with function view
    path("logs/class", views.LogList.as_view()),  # with class view
    path(
        "logs/class_generic", views.LogListGeneric.as_view()
    ),  # with class view with generics
    # the other endpoint below
    path("logs/<int:pk>/", views.log_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
