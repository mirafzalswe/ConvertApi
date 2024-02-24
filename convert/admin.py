from django.contrib import admin

from convert.models import ChoosePatternModel, ChoosePatternModelFile


# Register your models here.

@admin.register(ChoosePatternModel)
class ChoosePatternModelAdmin(admin.ModelAdmin):
    list_display = ('date', 'pattern', 'text')
    search_fields = ('text',)

@admin.register(ChoosePatternModelFile)
class ChoosePatternModelFileAdmin(admin.ModelAdmin):
    list_display = ('date', 'pattern', 'file')
    search_fields = ('file',)
