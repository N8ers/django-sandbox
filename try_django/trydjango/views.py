from django.http import HttpResponse


def home_view(request):

    HTML_STRING = """
        <h1>Allo</h1>
    """

    return HttpResponse(HTML_STRING)
