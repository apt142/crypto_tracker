from celery import Celery

from .constants import SUPPORTED_CATEGORIES
from .utils import fetch_crypto_data

app = Celery("crypto_tracker")


@app.task
def fetch_crypto_info():
    cryptos = SUPPORTED_CATEGORIES
    # We want to make each of these their own task so that
    # if one request fails or stalls it doesn't sink the whole set.
    for crypto in cryptos:
        fetch_crypto_info_by_id.delay(crypto["id"])


@app.task
def fetch_crypto_info_by_id(crypto_id):
    fetch_crypto_data(crypto_id)


# TODO: This doesn't work. I feel like I'm missing some
# small detail here. Leaving for documentation
app.conf.beat_schedule = {
    "schedule_fetch_crypo": {
        "task": "fetch_crypto_info",
        "schedule": 60.0,  # In seconds
    }
}
