from rest_framework.renderers import JSONRenderer
from rest_framework import serializers

from rest_framework import serializers
from .models import ChoosePatternModel, ChoosePatternModelFile


class ConvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoosePatternModel
        fields = ('text', 'pattern')


class ConvertSerializerFile(serializers.ModelSerializer):
    class Meta:
        model = ChoosePatternModelFile
        fields = ('file', 'pattern')



# class ConvertSerializer(ChoosePatternModelSerializer):
#     text = serializers.CharField()
#
#     class Meta(ChoosePatternModelSerializer.Meta):
#         model = Convert
#         fields = ChoosePatternModelSerializer.Meta.fields + ['text']
#
# class ConverTextSerializer(ChoosePatternModelSerializer):
#     file = serializers.FileField()
#
#     class Meta(ChoosePatternModelSerializer.Meta):
#         model = ConverText
#         fields = ChoosePatternModelSerializer.Meta.fields + ['file']
