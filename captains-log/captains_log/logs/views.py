from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics


from logs.models import Log
from logs.serializers import LogSerializer

# 2 ways of writing API views
# 1. @api_view decorator for function based views
# 2. APIView class for class based views


@api_view(["GET", "POST"])
def log_list(request):
    if request.method == "GET":
        logs = Log.objects.all()
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = LogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogList(APIView):
    def get(self, request, format=None):
        logs = Log.objects.all()
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogListGeneric(generics.ListCreateAPIView):
    queryset = Log.objects.all()
    serializer_class = LogSerializer


"""
The other endpoint below
"""


@api_view(["GET", "PUT", "DELETE"])
def log_detail(request, pk):

    try:
        log = Log.objects.get(pk=pk)
    except Log.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = LogSerializer(log)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = LogSerializer(log, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
