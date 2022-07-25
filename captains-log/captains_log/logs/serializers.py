from rest_framework import serializers
from logs.models import Log


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ["id", "star_date", "content"]
