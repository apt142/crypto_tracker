from rest_framework import serializers


class CurrencySpecificDatemSerializer(serializers.Serializer):
    crypto_id = serializers.CharField()
    currency = serializers.CharField()
    value = serializers.FloatField()


class CurrencySummarySerializer(serializers.Serializer):
    crypto_id = serializers.CharField()
    currency = serializers.CharField()
    stdev = serializers.FloatField()
    rank = serializers.IntegerField()
