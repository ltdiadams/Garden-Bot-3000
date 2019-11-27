from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os
# from django.db.models.signals import pre_save
# from django.dispatch import receiver
# import os
#
# class uploadfolder(models.Model):
#     """ my application """
#     File_to_upload = models.FileField(upload_to='')
#
# @receiver(pre_save, sender=uploadfolder)
# def file_update(sender, **kwargs):
#     upload_folder_instance = kwargs['instance']
#     if upload_folder_instance.File_to_upload:
#         path = upload_folder_instance.File_to_upload.path
#         os.remove(path)


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name, max_length=None):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

# class Media(models.Model):
#     name = models.CharField(u"Nome", max_length=128)
#     media = models.FileField(u"Arquivo", upload_to='', storage=OverwriteStorage())

class UploadFile(models.Model):
    # title = models.CharField()
    file = models.FileField(upload_to='', storage=OverwriteStorage())