from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("api/text/", views.ConvertAPIView.as_view(), name="user-list"),
    path("api/file/", views.ConvertFileAPIView.as_view(), name="text-convert"),
    path("", views.main_page, name="index")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)