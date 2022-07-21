from django.contrib import admin
from django.urls import path, include
from .views import (
    GetBoxes,
)


app_name = "core"
urlpatterns = [
    path('', GetBoxes.as_view()),
]
