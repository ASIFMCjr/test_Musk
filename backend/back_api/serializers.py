from rest_framework import serializers
from .models import NavItems, AdvantageTileItems

class NavItemsSerializer(serializers.ModelSerializer):
    nav_name = serializers.CharField(max_length=30)
    nav_link = serializers.CharField(max_length=50)
    nav_id   = serializers.IntegerField()

    class Meta:
        model = NavItems
        fields = ('__all__')

class AdvantageTileSerializer(serializers.ModelSerializer):
    adv_title_up   = serializers.CharField(max_length=50)
    adv_main       = serializers.CharField(max_length=4)
    adv_title_down = serializers.CharField(max_length=50)

    class Meta:
        model = AdvantageTileItems
        fields = ('__all__')