from django.urls import path
from . import views

urlpatterns = [
	path('',views.index),
	path('new',views.new),
	path('upload_file',views.upload_file)
]