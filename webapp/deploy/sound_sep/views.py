from django.shortcuts import render
# from .apps import WebappConfig
from django.core.files.storage import default_storage
import os


from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

def upload_file(request):
	if request.method == 'POST':
		file = request.FILES['audiofile.wav']
		# predicted_files = handle(file)
		file_name = default_storage.save(file.name, file)
		return render(request, 'sound_sep/base.html')

	else:
		return render(request, 'sound_sep/upload.html')



# def return_separation()