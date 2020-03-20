from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from .database import UserRegistrationForm
from .models import Notes
from django import forms
from django.core.mail import send_mail

def emailsend(request):
    send_mail('A message for MemeLord',
              'Stay strong, King. This is an automated message for you from your kingdom called "Мемi".',
              'eric199k@gmail.com',
              [forms.EmailField],
              fail_silently=False)
    return render(request, 'emailsend.html')

def contact(request):
    return render(request, 'contact.html')

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'singup.html')

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Oh, HI {username}!')
            return redirect(home)
    else:
        form = UserRegistrationForm()
    return render(request, 'lab1reg.html', {'form': form})

def notes_detail(request):
    note = Notes.objects.all().order_by('date');
    return render(request, 'create_note.html', { 'note': note })

def note_create(request):
    if request.method == 'POST':
        form = forms.CreateNote(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return render(request, 'home.html')
    else:
        form = forms.CreateNote()
    return render(request, 'create.html', { 'form': form })