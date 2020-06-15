from django.shortcuts import render, get_object_or_404, redirect
from .models import AppUser
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import default_storage
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
import os
# from django


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

def login_page(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.gt('password')
		person = authenticate(username = username, password = password)
		if person is not None:
			print("Login successfully done")
			login(request, person)

			return redirect('postlogin')

	

def serve_file(request):
	response = request.get('url')
	file = default_storage.open('Pattern recognitions Algorithms.pdf', 'rb').read()
	response['Content-Disposition'] = 'attachment; filename = audiofile.wav'
	return HttpResponse(file)
