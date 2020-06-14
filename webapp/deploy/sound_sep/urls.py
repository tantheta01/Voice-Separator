from . import views
from django.urls import path

urlpatterns = [
	path(r'upload/', views.upload_file, name = 'upload'),

	]