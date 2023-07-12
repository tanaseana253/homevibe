from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView
from django.urls import reverse_lazy, reverse
from homevibe.models import User, UserHistory, Photo
from homevibe.forms import SignupForm, SigninForm
from django.contrib.auth.forms import UserCreationForm


class HomeTemplateView(TemplateView):
    template_name = 'homepage.html'

class SignupView(CreateView):
    model = User
    form_class = SignupForm
    template_name = 'sign_up.html'
    success_url = reverse_lazy('login')

    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     user = form.save(commit=False)
    #     user.username = user.email
    #     user.save()
    #     return response

class InspirationTemplateView(TemplateView):
    template_name = 'inspiration.html'
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['photos'] = Photo.objects.all()
    #     return context

class PhotoListView(ListView):
    model = Photo
    template_name = 'photo_list.html'
    context_object_name = 'photos'

# def photo_list(request):
#     photos = Photo.objects.all()
#     return render(request, 'photo_list.html', {'photos': photos})










