COIN_GECKO_BASE_URL = "https://api.coingecko.com"


class Categories:
    BITCOIN = {"id": "bitcoin", "symbol": "btc", "name": "Bitcoin"}

    DOGECOIN = (
        {
            "id": "buff-doge-coin",
            "symbol": "dogecoin",
            "name": "Buff Doge Coin",
        },
    )


USD = "usd"
EUR = "eur"


CURRENCY_CHOICES = {
    "USD": USD,
    "EUR": EUR,
}


# from data_collection.utils import fetch_crypto_data
# fetch_crypto_data('bitcoin')
