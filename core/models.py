from django.db import models

# Create your models here.
class Files(models.Model):
    file = models.FileField(upload_to='store/datasets/')
    selectedOption = models.CharField(max_length=50, default='')
    target = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.file