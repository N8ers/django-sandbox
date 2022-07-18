from django.http import HttpResponse


def home_view(request):
    name = "tsuki"
    HTML_STRING = f"""
        <h1>Allo {name}</h1>
    """

    return HttpResponse(HTML_STRING)
