from django.db import models


class UploadedFile(models.Model):
    id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=255, null=False)
    file = models.FileField(null=False)
