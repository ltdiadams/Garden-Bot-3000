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

# dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

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

def parse_data(request):
    result_dict = {}
    last_dict = {}
    # csv_path = os.path.join(dir_path, "media/stored.csv")
    csv_path = os.path.join(dir_path, "media/values.csv")
    df1 = pd.read_csv(csv_path)
    a = df1[-1:]
    # last_dict["moisture"] = int(a["moisture"])
    # last_dict["time"] = a["time"].values[0]
    # last_dict["pump"] = int(a["pump"])
    # last_dict["light"] = int(a["light"])
    # last_dict["temperature"] = int(a["temperature"])
    #
    # result_dict["moisture"] = list(df1["moisture"])
    # result_dict["time"] = list(df1["time"])
    # result_dict["pump"] = list(df1["pump"])
    # result_dict["light"] = list(df1["light"])
    # result_dict["temperature"] = list(df1["temperature"])

    last_dict["time"] = a["time"].values[0]
    # last_dict["pump"] = int(a["pump"])
    last_dict["current_light"] = int(a["current_light"])
    last_dict["current_temp"] = int(a["current_temp"])
    last_dict["current_moist"] = int(a["current_moist"])

    # result_dict["moisture"] = list(df1["moisture"])
    # result_dict["time"] = list(df1["time"])
    # result_dict["pump"] = list(df1["pump"])
    # result_dict["light"] = list(df1["light"])
    # result_dict["temperature"] = list(df1["temperature"])

    result_dict["time"] = list(df1["time"])
    result_dict["current_light"] = list(df1["current_light"])
    result_dict["current_temp"] = list(df1["current_temp"])
    result_dict["current_moist"] = list(df1["current_moist"])

    return render(request, 'index.html', {'result_dict': result_dict, 'last_dict':last_dict})

# def new_csv(request):
#     data = {}
#     if "GET" == request.method:
#         return render(request, "newcsv.html", data)
#     # if not GET, then proceed
#     print("hey")
#     try:
#         file = request.FILES["csv_file"]
#         if not file.name.endswith('.csv'):
#             messages.error(request,'File is not CSV type')
#             return HttpResponseRedirect(reverse("dataset:new_csv"))
#             #if file is too large, return
#         if file.multiple_chunks():
#             messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
#             return HttpResponseRedirect(reverse("dataset:new_csv"))
#
#         # file = request.POST.get('csv_file', 'stored.csv')
#         # file = request.FILES["csv_file"]
#         csv_path = os.path.join(dir_path, "stored.csv")
#         # data = pd.read_csv(csv_path, header=None, skiprows=1, sep=",", delim_whitespace=True)
#         # df1 = {}
#         df1 = pd.read_csv(csv_path, sep=",", delim_whitespace=True)
#
#         #count = df1["threshold"].count()
#         #df1.loc[count ,"threshold"] = threshold
#         file_data = file.read().decode("utf-8")
#         lines = file_data.split("\n")
#         print("hello")
#         for line in lines:
#             print("howdy")
#             # line = convert_row(line)
#             fields = line.split(",")
#             # data = {}
#             df1["moisture"] = fields[0]
#             df1["time"] = fields[1]
#             df1["pump"] = fields[2]
#             df1["light"] = fields[3]
#             df1["temperature"] = fields[4]
#
#             try:
#                 form = EventsForm(df1)
#                 if form.is_valid():
#                     form.save()
#                 else:
#                     logging.getLogger("error_logger").error(form.errors.as_json())
#             except Exception as e:
#                 logging.getLogger("error_logger").error(repr(e))
#                 pass
#
#         # df1 = data
#         # csv_path = os.path.join(dir_path, "stored.csv")
#         df1.to_csv(csv_path, encoding='utf-8', index=True)
#
#     except Exception as e:
#         logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
#         messages.error(request,"Unable to upload file. "+repr(e))
#     print("there")
#     return render(request, 'newcsv.html', {'df1': df1})
#     # return HttpResponseRedirect(reverse("dataset:new_csv"))

# def convert_row( row ):
#     row_dict = {}
#     for key, value in row.items():
#         keyAscii = key.encode('ascii', 'ignore' ).decode()
#         valueAscii = value.encode('ascii','ignore').decode()
#         row_dict[ keyAscii ] = valueAscii
#     return row_dict

# def new_csv(request):
#     f = request.FILES["csv_file"]
#     csv_path = os.path.join(dir_path, "stored.csv")
#     df = pd.read_csv(f)
#     csv_path = os.path.join(dir_path, "stored.csv")
#     df.to_csv(csv_path, encoding='utf-8', index=False)
#
#     return render(request, 'newcsv.html')

# def new_csv(request):
#     if request.method=='POST':
#         form =uploadfileform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             # return render_to_response('upload_successful.html')
#     else:
#         form=uploadfileform()
#     return render(request, 'new_csv.html',{'form':form})

# def handle_uploaded_file(f):
#     with open('csv_file', 'wb+') as destination:
#         # for chunk in f.chunks():
#         #     destination.write(chunk)
#         csv_path = os.path.join(dir_path, "stored.csv")
#         df = pd.read_csv(f)
#         csv_path = os.path.join(dir_path, "stored.csv")
#         df.to_csv(csv_path, encoding='utf-8', index=False)

# def handle_uploaded_file(f):
#     # f = request.FILES["csv_file"]
#     csv_path = os.path.join(dir_path, "stored.csv")
#     df = pd.read_csv(f)
#     csv_path = os.path.join(dir_path, "stored.csv")
#     df.to_csv(csv_path, encoding='utf-8', index=False)
#
# def new_csv(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['csv_file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#         # csv_path = os.path.join(dir_path, "stored.csv")
#         # df = pd.read_csv(f)
#         # csv_path = os.path.join(dir_path, "stored.csv")
#         # df.to_csv(csv_path, encoding='utf-8', index=False)
#     return render(request, 'newcsv.html', {'form': form})

# def new_csv(request):
#     save_path = os.path.join(dir_path, 'stored.csv', request.FILES['csv_file'])
#     path = default_storage.save(save_path, request.FILES['csv_file'])
#     return default_storage.path(path)

class UploadFileView(FormView):
    template_name = 'newcsv.html'
    form_class = UploadFileForm

    def form_valid(self, form):
        my_file = UploadFile(
            file=self.get_form_kwargs().get('files')['file'])

        my_file.save()
        self.id = my_file.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('my_file', kwargs={'pk': self.id})

class UploadDetailView(DetailView):
    model = UploadFile
    template_name = 'dataset/upload_file.html'
    context_object_name = 'file'
#
# class UploadFileIndexView(ListView):
#     model = UploadFile
#     template_name = 'dataset/upload_file_view.html'
#     context_object_name = 'file'
#     queryset = UploadFile.objects.all()
