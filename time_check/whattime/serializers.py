from rest_framework import serializers


class TimeCheckSerializer(serializers.Serializer):
    time = serializers.IntegerField()
