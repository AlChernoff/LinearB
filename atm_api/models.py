from collections import defaultdict

from django.db import models


# # Create your models here.
# class Withdrawl(models.Model):
#     currency = models.CharField(max_length=5, blank=False, default='')
#     amount = models.DecimalField(max_digits=5, blank=False, default='', decimal_places=2)
#
from atm_api.Exceptions.TooMuchCoinsException import TooMuchCoinsException

BILL = 'BILL'
COIN = 'COIN'
INVENTORY_TYPES = [
    (BILL,"BILL"), (COIN, "COIN")]


class Inventory(models.Model):
    type = models.CharField(max_length=5, blank=False, null=False, choices=INVENTORY_TYPES)
    value = models.DecimalField(max_digits=6,decimal_places=2, blank=False, null=False)
    amount = models.IntegerField(blank=False, null=False, default=0)
    minimal_bill = 20

    @classmethod
    def get_inventory_choices(cls, amount: float) -> dict:
        result = {BILL: defaultdict(int), COIN: defaultdict(int)}
        # If needed - get bills
        if amount >= cls.minimal_bill:

            for bill in cls.objects.filter(type=BILL, value__lte=amount).order_by('value'):
                while True:
                    if amount - bill.value > 0:
                        amount -= bill.value
                        result[BILL][bill.value] += 1
                    else:
                        break

            if amount:

                for coin in cls.objects.filter(type=COIN, value__lte=amount).order_by('value'):
                    while True:
                        if amount - coin.value:
                            amount -= coin.value
                            result[COIN][coin.value] += 1
                            if result[COIN][coin.value] == 50:
                                raise TooMuchCoinsException("Sorry, amount of coins is more or equal 50")
                        else:
                            break

        return result


class Currency(models.Model):
    currency = models.CharField(max_length=8, blank=False, null=False)  # UNIQUE
    rate = models.DecimalField(max_digits=6,decimal_places=2, blank=False, null=False)

    @classmethod
    def get_currency_rate(cls, currency: str) -> float:
        return cls.objects.filter(currency=currency).first().rate

    @classmethod
    def add_currency_rate(cls, currency, rate):
        try:
            cls.objects.update_or_create(currency=currency, rate=rate)
        except Exception:
            pass
