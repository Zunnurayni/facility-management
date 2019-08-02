from django.shortcuts import render


def homepage(request):
	template = 'facilityapp/index.html'
	return render(request, template, {})

def services(request):
	template = 'facilityapp/services.html'
	return render(request, template, {})

def about(request):
	template = 'facilityapp/About us.html'
	return render(request, template, {})
	