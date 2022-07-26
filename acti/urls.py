from django.urls import path

from acti.views import writingFiles

urlpatterns = [
    path("", writingFiles, name="home")
]