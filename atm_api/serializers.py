from rest_framework import serializers
from atm_api.models import Currency

class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ('name')