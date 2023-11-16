from django.shortcuts import render
from django.http import JsonResponse
from .openapi import get_completion

def index(request):
    if request.method == 'POST':
        
        prompt = request.POST.get('prompt')
        print(prompt)
        response = get_completion(prompt)
        return JsonResponse({'response': response})
    
    return render(request, "index.html")