from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("relationship_app.urls")),
   path('example-form/', views.example_form_view, name='example_form'),
]