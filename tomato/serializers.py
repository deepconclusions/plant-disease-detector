from rest_framework import serializers


class TomatoSerializer(serializers.Serializer):
    prediction = serializers.IntegerField()
    label = serializers.CharField()
    confidence = serializers.FloatField()
    description = serializers.CharField()
    value_error = serializers.CharField()
