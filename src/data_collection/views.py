import logging
from datetime import timedelta
from statistics import stdev

from django.utils import timezone
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .constants import CURRENCY_CHOICES
from .constants import SUPPORTED_CATEGORIES
from .models import CurrencySpecificDatem
from .serializers import CurrencySpecificDatemSerializer
from .utils import fetch_crypto_data

logger = logging.getLogger(__name__)


class CurrencyViewSet(viewsets.ModelViewSet):
    serializer_class = CurrencySpecificDatemSerializer
    queryset = CurrencySpecificDatem.objects.all()

    @action(detail=False, url_path="analysis")
    def analysis(self, request):
        start_date = timezone.now()
        end_date = timezone.now() - timedelta(hours=24)
        calculated_data = []

        for crypto in SUPPORTED_CATEGORIES:
            for index, currency in CURRENCY_CHOICES.items():
                raw_data = CurrencySpecificDatem.objects.filter(
                    crypto_id=crypto["id"],
                    currency=currency,
                    created_at__lte=start_date,
                    created_at__gte=end_date,
                ).values_list("value", flat=True)

                logger.error(raw_data)

                calculated_data.append(
                    {
                        "crypto_id": crypto["id"],
                        "currency": currency,
                        "raw_data": raw_data,
                        "stdev": stdev(raw_data),
                    }
                )

        calculated_data = sorted(
            calculated_data, key=lambda item: item["stdev"], reverse=True
        )
        rank = 1
        for datem in calculated_data:
            datem["rank"] = rank
            rank = rank + 1

        return Response(calculated_data)

    @action(detail=False, url_path="pull")
    def pull(self, request):
        for crypto in SUPPORTED_CATEGORIES:
            fetch_crypto_data(crypto["id"])

        return Response(True)
