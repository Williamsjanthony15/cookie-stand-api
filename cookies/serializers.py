from rest_framework import serializers
from .models import Cookie, CookieStand


class CookieSerializer(serializers.ModelSerializer):
    class Meta:
        model = CookieStand
        fields = "__all__"
