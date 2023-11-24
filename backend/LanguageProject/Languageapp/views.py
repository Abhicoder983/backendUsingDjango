from django.shortcuts import render
from django.http import HttpResponse
from .serializers import studentSerializer
from rest_framework.generics import ListAPIView
from .models import student


# Create your views here.
class studentlist(ListAPIView):
    queryset=student.objects.all()
    serializer_class=studentSerializer
def landing(request):
    return render(request ,'index.html')
def contactform(request):
    return render(request ,'contactform.html')


