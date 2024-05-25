from django.urls import path
from . import views

urlpatterns = [
    path("wordcounter/", views.word_counter, name='wordcounter'),
    path("", views.home, name='home')
]