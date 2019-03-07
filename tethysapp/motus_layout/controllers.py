from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    context = {}
    return render(request, 'motus_layout/home.html', context)

@login_required()
def Motus_Map(request):
    context = {}
    return render(request, 'motus_layout/Motus_Map.html', context)