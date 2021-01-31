from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from user.forms import UserLoginForm
from django.contrib.auth import login, logout


class UserLoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('schemas')
        form = UserLoginForm()
        template = 'user/login.html'
        context = {'form': form}
        return render(request, template, context=context)

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        template = 'user/login.html'
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('schemas')

        else:
            context = {'form': form}
            return render(request, template, context=context)


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')
