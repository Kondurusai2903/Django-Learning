from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'I am indexpage.......')



def about(request):
    return render(request, 'I am aboutpage.......')