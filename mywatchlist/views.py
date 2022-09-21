from django.shortcuts import render
from mywatchlist.models import Barangmywatchlist
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    data_watchlist = Barangmywatchlist.objects.all()
    context = {
        'list_data_watchlist':data_watchlist,
        'nama': 'Rafli Wasis Anggito',
        'npm' : '2106751442'
    }

    return render(request, "watchlist.html", context)

def show_xml(request):
    data = Barangmywatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Barangmywatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request,id):
    data = Barangmywatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request,id):
    data = Barangmywatchlist.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")