from django.shortcuts import render, redirect, HttpResponse
from .models import User
# Create your views here.

def index(request):
      User.userManager.login("speros@codingdojo.com", "Speros")
      return HttpResponse(User.userManager.login("speros@codingdojo.com", "Speros"))
