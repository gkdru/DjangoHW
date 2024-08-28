from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import UserProfile
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from freedjango.settings import BASE_DIR

def succes(request):
    up = UserProfile.objects.last()

    return render(request, 'userpofile/succes.html', {'up':up,})
    

class ProfilereateView(CreateView):
    model = UserProfile
    fields = "__all__"
    template_name = 'userpofile/profileform.html'

    def get_success_url(self) -> str:
        return reverse('up:succes')
    
