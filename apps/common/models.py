import os

from decimal import getcontext

from django.db import models
from django.utils import timezone


getcontext().prec = 10


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    model_created_at = models.DateTimeField(default=timezone.now)
    model_modified_at = AutoDateTimeField(default=timezone.now)

    class Meta:
        abstract = True
        ordering = ["model_created_at"]


def file_upload_path(instance, filename):
    # Determine the folder dynamically, e.g., based on a model attribute
    folder_name = instance.__class__.__name__

    # Construct the upload path
    upload_path = os.path.join(folder_name, filename)

    return upload_path
