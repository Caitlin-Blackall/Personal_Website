from django.shortcuts import render
from about_me.models import Profile

# Create your views here.
# create a query to retrieve all objects in the profile table
# define context dictionary
# render the template with context as an argument
def about_me(request):
   profile = Profile.objects.all()
   context = {
      'profile': profile
   }

   return render(request, 'about_me.html', context)