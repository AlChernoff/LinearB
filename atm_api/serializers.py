from rest_framework import serializers
from atm_api.models import Currency, Withdrawl


class WithdrawlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Withdrawl
        fields = ('currency',
                  'amount')

class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ('name')