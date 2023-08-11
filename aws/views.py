from django.shortcuts import render

# Create your views here.
def aws(request):
    return render(request, 'aws.html')