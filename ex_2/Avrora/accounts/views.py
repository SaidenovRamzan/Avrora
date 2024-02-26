from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from accounts.forms import LoginForm


class CustomLoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "registration/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been successfully logged in.")
                return redirect("/")
            else:
                messages.error(request, "Invalid email or password.")
        return render(request, "registration/login.html", {"form": form})


class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        messages.success(request, "You have been successfully logged out.")
        return redirect("/")
