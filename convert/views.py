from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from .models import ChoosePatternModel, ChoosePatternModelFile
from .serializers import ConvertSerializer, ConvertSerializerFile

from .txtconvert import convert_latin, convert_file

class ConvertAPIView(generics.CreateAPIView):
    serializer_class = ConvertSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data['text']
        to_type = serializer.validated_data['pattern']
        converted_text = convert_latin(text, to_type)
        return Response({'converted_text': converted_text}, status=status.HTTP_200_OK)


class ConvertFileAPIView(generics.CreateAPIView):
    serializer_class = ConvertSerializerFile

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        to_type = serializer.validated_data['pattern']
        converted_file = convert_file(to_type, file)
        return Response({'converted_text': converted_file}, status=status.HTTP_200_OK)


def main_page(request):
    return HttpResponse('''
   <br>  for text 
   <br>  <h3> /api/text </h3>
   <br>  for file
   <br>  <h3> /api/file </h3>
    ''')


from django.shortcuts import render

# Create your views here.
