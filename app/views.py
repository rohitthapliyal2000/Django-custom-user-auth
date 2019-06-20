from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from .models import User
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login, logout


@csrf_exempt
def signup(request):
	# logout(request)
	body_unicode = request.body.decode("utf-8")
	body = json.loads(body_unicode)
	name = body['name']
	email = body['email']
	password = body['password']
	try:
		user = User.objects.create_user(name=name, email=email, password=password)
		print(user)
		token = Token.objects.create(user=user)
		return JsonResponse({'success': True, 'Token': token.key})
	except Exception:
		return JsonResponse({'success': False})

@csrf_exempt
def signin(request):
	body_unicode = request.body.decode("utf-8")
	body = json.loads(body_unicode)
	email = body['email']
	password = body['password']
	user = authenticate(email=email, password=password)
	if user is not None:
		login(request, user)
		token = Token.objects.get(user=user)
		return JsonResponse({'success': True, 'Token': token.key})
	else:
		return JsonResponse({'success': False})

@csrf_exempt
def details(request):
	# body_unicode = request.body.decode("utf-8")
	# body = json.loads(body_unicode)
	# email = body['email']
	# password = body['password']
	# user = authenticate(email=email, password=password)
	if request.user.is_anonymous is False:
		return JsonResponse({'success': True, 'name': request.user.name, 'email': request.user.email})
	else:
		return JsonResponse({'success': False})

@csrf_exempt
def update(request):
	body_unicode = request.body.decode("utf-8")
	body = json.loads(body_unicode)
	name = body['name']
	email = body['email']
	password = body['password']
	if request.user.is_anonymous is False:
		try:
			user = request.user
			user.name = name
			user.email = email
			user.set_password(password)
			user.save()
			return JsonResponse({'success': True})
		except Exception:
			return JsonResponse({'success': False})
	return JsonResponse({'success': False})
		