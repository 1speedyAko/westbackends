from django.http import JsonResponse

def home(request):
	return JsonResponse({'info': 'fullstack ecom','name':'westk9'})