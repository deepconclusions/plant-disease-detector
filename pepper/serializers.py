from rest_framework import serializers


class PepperSerializer(serializers.Serializer):
    Prediction = serializers.CharField()
    ValueError = serializers.CharField()
