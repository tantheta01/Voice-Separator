from . import views
from django.urls import path

urlpatterns = [
	path(r'upload/', views.upload_file, name = 'upload'),

	


	path("", views.homepage, name="homepage"),
	path(r'download/', views.show_download_files, name = 'show_download'),
	path(r'download/<str:path>', views.download_file, name="download_file"),

	]