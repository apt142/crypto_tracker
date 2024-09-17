from celery import shared_task

from .constants import Categories
from .utils import fetch_crypto_data


@shared_task
def fetch_crypto_info():
    crypto_ids = [Categories.BITCOIN, Categories.DOGECOIN]
    # We want to make each of these their own task so that
    # if one request fails or stalls it doesn't sink the whole set.
    for id in crypto_ids:
        fetch_crypto_info_by_id.delay()


@shared_task
def fetch_crypto_info_by_id(crypto_id):
    fetch_crypto_data(crypto_id)
