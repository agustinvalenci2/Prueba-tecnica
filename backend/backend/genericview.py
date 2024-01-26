from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from .models import *
from django.shortcuts import redirect
from django.contrib.auth import login as log_in
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json