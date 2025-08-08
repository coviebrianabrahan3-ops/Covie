from django.shortcuts import render, redirect
from .models import Part

def home(request):
    return redirect('search_parts')

def search_parts(request):
    query = request.GET.get('q')
    results = []

    if query:
        results = Part.objects.filter(part_number__icontains=query)

    return render(request, 'parts/search.html', {'results': results, 'query': query})
