from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import ChoosePatternModel, ChoosePatternModelFile


class ConvertAPITestCase(APITestCase):

    def test_text_conversion_cyrillic_to_latin(self):
        # Test text conversion from cyrillic to latin
        url = reverse('convert-text-api')
        data = {'text': 'Привет мир', 'pattern': 'latin'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['converted_text'], 'Privet mir')

    def test_text_conversion_invalid_pattern(self):
        # Test text conversion with an invalid pattern
        url = reverse('convert-text-api')
        data = {'text': 'Hello world', 'pattern': 'invalid_pattern'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


    def test_file_conversion_latin_to_cyrillic(self):
        # Test file conversion from latin to cyrillic
        url = reverse('convert-file-api')
        file_content = 'Hello world'
        file_data = {'file': file_content, 'pattern': 'cyrillic'}

        response = self.client.post(url, file_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['converted_text'], 'Хелло ворлд')

    # Add more test cases as needed based on your specific requirements

