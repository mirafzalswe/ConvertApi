from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ChoosePatternModel, ChoosePatternModelFile


class ConvertAPITestCase(APITestCase):

    def test_text_conversion_cyrillic_to_latin(self):
        url = reverse('text-convert')
        txt = '''
        Тошкент — Ўзбекистоннинг пойтахти ва енг йирик шаҳри бўлиб, аҳолиси бўйича 
        Марказий Осиёдаги енг йирик қадимий шаҳарлардан бири ҳисобланади.
        '''
        cyrillic_txt  = '''
        Toshkent — Oʻzbekistonning poytaxti va eng yirik shahri boʻlib, aholisi boʻyicha 
        Markaziy Osiyodagi eng yirik qadimiy shaharlardan biri hisoblanadi. 
        '''
        data = {'text': 'Привет мир', 'pattern': 'latin'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['converted_text'], cyrillic_txt)

    def test_text_conversion_invalid_pattern(self):
        url = reverse('text-convert')
        data = {'text': 'Hello world', 'pattern': 'invalid_pattern'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_file_conversion_latin_to_cyrillic(self):
        url = reverse('file-convert')
        file_content = '''
        Toshkent shahrining YIMi $2,74 milliardni tashkil etadi va bu koʻrsatkich 
         Oʻzbekistondagi eng katta YIMga ega shahar boʻlib kelmoqda.
        '''
        file_data = {'file': file_content, 'pattern': 'cyrillic'}
        response = self.client.post(url, file_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['converted_text'], '''Тошкент шаҳрининг ЙИМи $2,74 миллиардни ташкил етади ва бу кўрсаткич 
        Ўзбекистондаги енг катта ЙИМга ега шаҳар бўлиб келмоқда.''')

