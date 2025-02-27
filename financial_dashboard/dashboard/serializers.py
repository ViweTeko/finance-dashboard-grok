from rest_framework import serializers
from .models import FinancialData, AssetClass

class AssetClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetClass
        fields = '__all__'

class FinancialDataSerializer(serializers.ModelSerializer):
    asset_class = AssetClassSerializer()

    class Meta:
        model = FinancialData
        fields = '__all__'