from django.db import models

class AssetClass(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class FinancialData(models.Model):
    date = models.DateField()
    asset_class = models.ForeignKey(AssetClass, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        unique_together = ['date', 'asset_class']