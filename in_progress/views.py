from django.shortcuts import render
from in_progress.models import In_Progress

# Create your views here.
def in_progress(request):
    posts = In_Progress.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(request, 'in_progress.html', context)