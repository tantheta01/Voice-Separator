from django.shortcuts import render, get_object_or_404, redirect
from .models import AppUser
from django.contrib.auth import authenticate, login, logout
from django.core.files.storage import default_storage
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .separator import separate
import os


from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

def homepage(request):
	return render(request, 'sound_sep/homepage.html',{})

def upload_file(request):
	if request.method == 'POST':
		file = request.FILES['audiofile.wav']
		# predicted_files = handle(file)
		file_name = default_storage.save(file.name, file)
		request.session['upload_file_name']=file.name 	#make unique using user id or session id
		return redirect("show_download")
	else:
		return render(request, 'sound_sep/upload.html')

def show_download_files(request):
	file_available=True
	try:
		file_name=request.session['upload_file_name']
		if not default_storage.exists(file_name):
			file_available=False
	except:
		file_available=False
	if file_available:
		# with open("media/"+file_name, 'rb') as fh:
		# 	response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
		# 	response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_name)
		# 	return response
		f_vocals,f_bass,f_drum,f_others=separate(file_name)
	else:
		f_vocals,f_bass,f_drum,f_others=None, None, None, None
	list_of_paths=[f_vocals, f_bass, f_drum, f_others]
	return render(request, 'sound_sep/download.html',{"file_available": file_available, "pathlist": list_of_paths})

def download_file(request, path):
	actual_path="media/"+path
	with open(actual_path, 'rb') as fh:
		response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
		response['Content-Disposition'] = 'inline; filename=' + os.path.basename(actual_path)
		return response

def login_page(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		person = authenticate(username = username, password = password)
		if person is not None:
			print("Login successfully done")
			login(request, person)

			return redirect('postlogin')

	
