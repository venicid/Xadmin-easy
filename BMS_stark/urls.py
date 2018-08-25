
from django.contrib import admin
from django.urls import path

from app01 import views

from stark.service import stark
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('stark/', ([],None,None)),
    path('stark/', stark.site.urls),
    path('index/', views.index),
    path('add/', views.add),
]
