from rest_framework import serializers


class CornSerializer(serializers.Serializer):
    prediction = serializers.IntegerField()
    label = serializers.CharField()
    confidence = serializers.FloatField()
    description = serializers.CharField()
    value_error = serializers.CharField()
