from rest_framework import serializers


class CornSerializer(serializers.Serializer):
    Prediction = serializers.CharField()
    ValueError = serializers.CharField()
