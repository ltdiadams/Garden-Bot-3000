from django.shortcuts import render
import pandas as pd
import os 

dir_path = os.path.dirname(os.path.realpath(__file__))

def fill_threshold(request):
    threshold = request.POST.get('threshold')
    csv_path = os.path.join(dir_path, "stored.csv")
    df1 = pd.read_csv(csv_path) 
    count = df1["threshold"].count()
    df1.loc[count ,"threshold"] = threshold
    csv_path = os.path.join(dir_path, "stored.csv")
    df1.to_csv(csv_path, encoding='utf-8', index=False)

    return render(request, 'threshold.html')

def parse_data(request):
    result_dict = {}
    last_dict = {}
    csv_path = os.path.join(dir_path, "stored.csv")
    df1 = pd.read_csv(csv_path) 
    a = df1[-1:]
    last_dict["moisture"] = int(a["moisture"])
    last_dict["time"] = a["time"].values[0]
    last_dict["pump"] = int(a["pump"])
    last_dict["light"] = int(a["light"])
    last_dict["temperature"] = int(a["temperature"])

    result_dict["moisture"] = list(df1["moisture"])
    result_dict["time"] = list(df1["time"])
    result_dict["pump"] = list(df1["pump"])
    result_dict["light"] = list(df1["light"])
    result_dict["temperature"] = list(df1["temperature"])
    return render(request, 'index.html', {'result_dict': result_dict, 'last_dict':last_dict})

