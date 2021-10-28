from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils.http import is_safe_url
from django.views import View
from django.views.generic import ListView, DetailView
from django.utils import timezone

from synology_video import settings
from .forms import LoginForm
from .models import Records
from .utils import insert_in_database


@login_required()
@permission_required(perm='records.add_records', raise_exception=True)
def insert_in_base(request):
    insert_in_database()
    return HttpResponse('Data upload at base')


class RecordsList(LoginRequiredMixin, ListView):
    model = Records
    # paginate_by = 20

    def get_queryset(self):
        return Records.objects.filter(date__lte=timezone.now()).filter(public=True)


class VideoList(LoginRequiredMixin, ListView):
    model = Records
    # paginate_by = 20

    def get_queryset(self):
        return Records.objects.filter(date__lte=timezone.now()).filter(public=True).filter(type='video')


class FilesList(LoginRequiredMixin, ListView):
    model = Records
    # paginate_by = 20

    def get_queryset(self):
        return Records.objects.filter(date__lte=timezone.now()).filter(public=True).filter(type='doc')


class RecordDetail(LoginRequiredMixin, DetailView):
    model = Records

    def get(self, request, *args, **kwargs):
        context = super(RecordDetail, self).get(request, *args, **kwargs)
        self.object.count_views += 1
        self.object.save()
        return context


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('records:home'))
        form = LoginForm(initial={'username': '', 'password': ''})
        return render(request, 'registration/login.html')

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None and user.is_active:
                login(request, user)
                # return HttpResponseRedirect(reverse('home'))
                redirect_to = request.GET.get('next', '/')
                if is_safe_url(url=redirect_to, allowed_hosts=settings.ALLOWED_HOSTS):
                    return HttpResponseRedirect(redirect_to)
            else:
                messages.error(request, 'Username or password is incorrect')
                return render(request, 'registration/login.html')


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('records:login'))
