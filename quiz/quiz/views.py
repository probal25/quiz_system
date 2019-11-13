# This file contains index views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        return Response(data={'message': 'Hello from GET'}, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        return Response(data=request.data, status=status.HTTP_200_OK)
    else:
        return Response(data="Request Method is not right")


class Message(APIView):

    def get(self, request):
        return Response(data="Class Based View", status=status.HTTP_200_OK)

    def post(self, request):
        return Response(data="Hit by POST request", status=status.HTTP_200_OK)
