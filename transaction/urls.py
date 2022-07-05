from django.urls import path
from .views import transaction_all


urlpatterns = [
    path('list/', transaction_all , name='transaction-list')
    ]