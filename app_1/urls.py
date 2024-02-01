from django.contrib import admin
from django.urls import path
from app_1 import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('book', views.insertRecord, name='insertRecord'),  # for function based view
    path('book',views.bookListAPI.as_view())            # for class based view
]