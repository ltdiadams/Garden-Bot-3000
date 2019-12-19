# Growbot: create upload form for webapp
# To be deployed as a public webapp

# Logan DiAdams,
# For PHYS/COMP-3361
# 2019

from django import forms

# makes upload form ready for rendering

class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField(label="Select a file to upload")