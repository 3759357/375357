from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'food/index.html')

def result(request):
    return render(request,'food/result.html')