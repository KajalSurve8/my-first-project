from django.db import models

# Create your models here.
class MedicineData(models.Model):
    srno = models.AutoField(auto_created=True, primary_key=True)
    pname = models.CharField(max_length=30)
    batchid = models.CharField(max_length=30)
    lotno = models.CharField(max_length=30)
    mandate = models.DateField()
    exdate = models.DateField()
    protocolid = models.CharField(max_length=30)