from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.utils import timezone
from .models import Records
from .utils import insert_in_database


def insert_in_base(request):
    insert_in_database()
    return HttpResponse('Data upload at base')


class RecordsList(ListView):
    model = Records
    # paginate_by = 20

    def get_queryset(self):
        return Records.objects.filter(time_create__lte=timezone.now()).filter(public=True)


class RecordDetail(DetailView):
    model = Records
