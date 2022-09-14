from django.shortcuts import render

# Create your views here.
def enfermerasJefe(request):
    return render(request, "EnfermerasJefe/index-chief-nursing.html")