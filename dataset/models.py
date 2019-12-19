# Growbot: create models for webapp
# To be deployed as a public webapp

# Logan DiAdams,
# For PHYS/COMP-3361
# 2019

# import libraries

from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

# -----------------------------------------------------------------------------
# overwrite csv file in MEDIA if csv file uploaded already exists

class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

# -----------------------------------------------------------------------------
# maps file to MEDIA

class UploadFile(models.Model):
    # title = models.CharField()
    file = models.FileField(upload_to='', storage=OverwriteStorage())