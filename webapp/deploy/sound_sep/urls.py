from . import views
from django.urls import path

urlpatterns = [
	path(r'upload/', views.upload_file, name = 'upload'),
	path(r'downl/', views.serve_file, name = 'serve'),

	]