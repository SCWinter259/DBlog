from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm

# Create your views here.

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()

        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        # the request carries the data that we need for that post request
        # the request would contain info from all of the fields defined in forms.py
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')