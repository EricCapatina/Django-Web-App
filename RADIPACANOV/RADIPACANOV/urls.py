from django.contrib import admin
from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('signup/', auth_views.LoginView.as_view(template_name='singup.html'), name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', auth_views.LogoutView.as_view(template_name='home.html'), name='logout'),
    path('create/', views.notes_detail, name="create"),
    path('create_note/', views.note_create, name='create_note'),
    path('contact/', views.contact, name='contact'),
    path('emailsend/', views.emailsend, name='emailsend'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', views.home, name='home')
]