from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import timedelta

# Create your views here.
def main(request):
    return render(request, "nasa/index.html")

def scoring(request):
    data = pd.read_csv('scoring/data.csv')

    data.drop(
        labels=["transect_source_fire_ID", "transect_type", "transect_source_fire_type", "transect_MCE", "transect_source_fire_alt", "transect_source_fire_lat", "transect_plume_number","transect_source_fire_long", "transect_structures_boolean", "transect_suppresion_boolean", "transect_fuel", "transect_ignition"],
        axis="columns"
    )

    data.head()
    x = data["transect_smoke_age (s)"].values[:5].reshape(-1, 1)
    y = data["transect_windspeed (m/s)"].values[:5].reshape(-1, 1)
    start_time = data["transect_start_time (UTC s from midnight)"].values[0]
    end_time = data["transect_end_time  (UTC s from midnight)"].values[0]
    co2 = data["transect_BG_CO2(ppm)"].values[0]
    windspeed = data["transect_smoke_age (s)"].values[0]

    reg = LinearRegression()

    reg.fit(x, y)

    dat = str(int(reg.score(x, y) * 100))
    start = str(timedelta(seconds=start_time))
    end = str(timedelta(seconds=end_time))[:8]
    return render(request, "nasa/scoring.html", {
        "dat": dat,
        "start": start,
        "end": end,
        "date": "25.07",
        "co2": str(int(co2)),
        "windspeed": int(windspeed)
    })
    
def about(request):
    return render(request, "nasa/about.html")

def weather(request):
    return render(request, "nasa/weatherapp.html")

def developers(request):
    return render(request, "nasa/dvelopers.html")