# Growbot: create views for webapp
# To be deployed as a public webapp

# Logan DiAdams,
# For PHYS/COMP-3361
# 2019

# ------------------------------------------------------------------------------
# import libraries

from django.http import HttpResponseRedirect
from django.shortcuts import render
from tablib import Dataset
import pandas as pd
import os
import csv
import logging
from django.contrib import messages
from django import forms

from .forms import UploadFileForm
from .models import UploadFile

from django.urls import reverse
from django.views.generic import FormView, DetailView, ListView
from django.conf import settings

from django.core.files.storage import FileSystemStorage

# path to file

# dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


# ------------------------------------------------------------------------------
# test function for writing a new column to the csv, not used

def fill_threshold(request):
    threshold = request.POST.get('threshold')
    # csv_path = os.path.join(dir_path, "media/stored.csv")
    csv_path = os.path.join(dir_path, "media/values.csv")
    df1 = pd.read_csv(csv_path)
    count = df1["threshold"].count()
    df1.loc[count ,"threshold"] = threshold
    # csv_path = os.path.join(dir_path, "media/stored.csv")
    csv_path = os.path.join(dir_path, "media/values.csv")
    df1.to_csv(csv_path, encoding='utf-8', index=False)

    return render(request, 'threshold.html')

# ------------------------------------------------------------------------------
# function for getting data from the csv to be used in charts

def parse_data(request):
    result_dict = {}
    last_dict = {}
    # csv_path = os.path.join(dir_path, "media/stored.csv")
    csv_path = os.path.join(dir_path, "media/values.csv")
    df1 = pd.read_csv(csv_path)
    a = df1[-1:]

    last_dict["time"] = a["time"].values[0]
    last_dict["current_light"] = int(a["current_light"])
    last_dict["current_temp"] = int(a["current_temp"])
    last_dict["current_moist"] = int(a["current_moist"])

    result_dict["time"] = list(df1["time"])
    result_dict["current_light"] = list(df1["current_light"])
    result_dict["current_temp"] = list(df1["current_temp"])
    result_dict["current_moist"] = list(df1["current_moist"])

    return render(request, 'index.html', {'result_dict': result_dict, 'last_dict':last_dict})

# ------------------------------------------------------------------------------
# new view class for the upload form

class UploadFileView(FormView):
    template_name = 'newcsv.html'
    form_class = UploadFileForm

    def form_valid(self, form):
        my_file = UploadFile(
            file=self.get_form_kwargs().get('files')['file'])

        my_file.save()
        self.id = my_file.id

        return HttpResponseRedirect(self.get_success_url())

    # file is uploaded, url returned is specific to file name and primary key

    def get_success_url(self):
        return reverse('my_file', kwargs={'pk': self.id})

class UploadDetailView(DetailView):
    model = UploadFile
    template_name = 'dataset/upload_file.html'
    context_object_name = 'file'