from django.db import models

# Create your models here.

class VehicleModel(models.Model):
    uid = models.AutoField(primary_key=True, db_column='uid')
    vechno = models.CharField(max_length=10, db_column='vechno', unique=True, null=False)
    vechmodel = models.CharField(max_length=30, db_column='vechmodel', null=True)
    vechcompany = models.CharField(max_length=50, db_column='vechcompany', null=False)
    manuyear = models.IntegerField(db_column='manuyear', null=True)
    color = models.CharField(max_length=10, db_column='color', null=True)
    mileage = models.DecimalField(db_column='mileage', max_digits=5, decimal_places=2, null=True)
    active = models.BooleanField(db_column='active', default=True, null=True)

    def __str__(self):
        return self.uid

    class Meta:
        managed = True
        db_table = 'vehicle'