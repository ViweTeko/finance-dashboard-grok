from django.db.models import Sum
from rest_framework import viewsets, filters
from rest_framework.response import Response
from .models import FinancialData, AssetClass
from .serializers import FinancialDataSerializer, AssetClassSerializer
from django_filters.rest_framework import DjangoFilterBackend
import pandas as pd
from django.shortcuts import render

def index(request):
    return render(request, 'dashboard/index.html')

class AssetClassViewSet(viewsets.ModelViewSet):
    queryset = AssetClass.objects.all()
    serializer_class = AssetClassSerializer

class FinancialDataViewSet(viewsets.ModelViewSet):
    queryset = FinancialData.objects.all()
    serializer_class = FinancialDataSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['date', 'asset_class']
    ordering_fields = ['date']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        granularity = request.query_params.get('granularity', 'D')  # Default to daily
        asset_classes = request.query_params.getlist('asset_classes')

        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])

        if asset_classes:
            queryset = queryset.filter(asset_class__name__in=asset_classes)

        data = queryset.values('date', 'asset_class__name').annotate(total_value=Sum('value')).order_by('date')

        df = pd.DataFrame(list(data))
        if not df.empty:
            df['date'] = pd.to_datetime(df['date'])
            df = df.pivot(index='date', columns='asset_class__name', values='total_value').fillna(0)

            if granularity == 'W':
                df = df.resample('W').sum()
            elif granularity == 'M':
                df = df.resample('M').sum()
            elif granularity == 'Q':
                df = df.resample('Q').sum()
            elif granularity == 'A':
                df = df.resample('A').sum()

            df.reset_index(inplace=True)
            df['date'] = df['date'].dt.strftime('%Y-%m-%d')
            data_dict = df.to_dict(orient='records')
        else:
            data_dict = []

        return Response(data_dict)
