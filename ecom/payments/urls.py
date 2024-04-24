from django.urls import path
from . import views

urlpatterns = [
    path('payments_success', views.payments_success, name='payments_success'),
    path('checkout', views.checkout, name='checkout'),
    path('billing_info', views.billing_info, name='billing_info'),
    path('process_order', views.process_order, name='process_order'),
]
