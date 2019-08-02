from django.shortcuts import render


def homepage(request):
	template = 'facilityapp/index.html'
	return render(request, template, {})