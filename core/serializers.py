from rest_framework import serializers

from core.models import Riddle


class RiddleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Riddle
        fields = "__all__"