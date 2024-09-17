from django.db import models

from .constants import CURRENCY_CHOICES


class RawCurrencySnapshot(models.Model):
    crypto_id = models.CharField(max_length=128)
    payload = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)

    def get_value_by_currency(self, currency):
        if (
            "market_data" in self.payload
            and "current_price" in self.payload["market_data"]
        ):
            return self.payload["market_data"]["current_price"].get(currency)

        return None

    def build_currency_specific(self):
        # TODO: If we rebuild, do we want to clear out old ones first
        # and then rebuild?
        for index, currency in CURRENCY_CHOICES.items():
            data_point = CurrencySpecificDatem(
                crypto_id=self.crypto_id,
                currency=currency,
                value=self.get_value_by_currency(currency),
                raw_data=self,
            )
            data_point.save()


class CurrencySpecificDatem(models.Model):
    crypto_id = models.CharField(max_length=128, db_index=True)
    currency = models.CharField(db_index=True)
    value = models.FloatField()
    raw_data = models.ForeignKey(
        "RawCurrencySnapshot", on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(auto_now_add=True)
