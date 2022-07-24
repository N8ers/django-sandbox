from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    # Url patterns for FUNCTION based views
    # path("snippets/", views.snippet_list),
    # path("snippets/<int:pk>/", views.snippet_detail),
    # Url patterns for CLASS based views
    path("snippets/", views.SnippetList.as_view()),
    path("snippets/<int:pk>/", views.SnippetDetail.as_view()),
    path("users/", views.UserList.as_view()),
    path("users/<int:pk>/", views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
