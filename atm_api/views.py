from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from atm_api.models import Currency, Inventory
from atm_api.serializers import CurrencySerializer

from rest_framework.decorators import api_view


@api_view(['POST'])
def withdrawl(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        withdrawl_serialiser = WithdrawlSerializer(data=request_data)

        if request_data.is_valid():
            amount = Currency.get_currency_rate(currency=request_data['currency']) * request_data['amount']
            inventory_choices = Inventory.get_inventory_choices(amount=amount)
            return JsonResponse(inventory_choices, status=status.HTTP_200_OK)

        return JsonResponse(withdrawl_serialiser.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required
@api_view(['POST'])
def add_currency(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        currency_serialiser = CurrencySerializer(data=request_data)

        if request_data.is_valid():
            Currency.add_currency_rate(currency=request_data['currency'], rate=request_data['rate'])
            return JsonResponse(currency_serialiser.data, status=status.HTTP_201_CREATED)

        return JsonResponse(currency_serialiser.errors, status=status.HTTP_400_BAD_REQUEST)
