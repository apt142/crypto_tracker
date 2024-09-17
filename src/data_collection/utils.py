import requests
from django.conf import settings

from .constants import COIN_GECKO_BASE_URL
from .models import RawCurrencySnapshot


def request_pairing(crypto_id):
    url = f"{COIN_GECKO_BASE_URL}/api/v3/coins/{crypto_id}"
    headers = {
        "Content-Type": "application/json",
        "x-cg-demo-api-key": settings.COIN_GECKO_API_KEY,
    }

    response = requests.get(url, headers=headers)
    return response.json()


def fetch_crypto_data(crypto_id):
    raw_data = request_pairing(crypto_id)

    # Store Raw Data
    snapshot = RawCurrencySnapshot(crypto_id=crypto_id, payload=raw_data)
    snapshot.save()

    # Build granular data
    snapshot.build_currency_specific()
