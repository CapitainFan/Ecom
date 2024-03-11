from django.shortcuts import render

def payments_success(request):
	return render(request, 'payments/payments_success.html', {})
