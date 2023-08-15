from django.shortcuts import render

# Create your views here.
def in_progress(request):
    return render(request, 'in_progress.html')