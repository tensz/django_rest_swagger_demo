from django.db import models


# Create your models here.
class ResourceModel(models.Model):
    id = models.AutoField(primary_key=True)
    resource_id = models.CharField(max_length=50, db_index=True, unique=True)
    resource_remark = models.CharField(max_length=50)
