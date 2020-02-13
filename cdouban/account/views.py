from django.shortcuts import render

# Create your views here.

def people(request):
	return render(request, 'people.html')