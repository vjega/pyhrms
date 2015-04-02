from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
# Create your views here.

class dashboard(View):
    def get(self, request):
        return render(request, 'index.html')

class requisition(View):
    def get(self, request):
        return render(request, 'requisition.html')

class candidates(View):
    def get(self, request):
        return render(request, 'candidates.html')

class intw_schedules(View):
    def get(self, request):
        return render(request, 'intw_schedules.html')

class employees(View):
    def get(self, request):
        return render(request, 'employees.html')