from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_barang_katalog,
    'nama': 'Rafli Wasis Anggito',
    'npm' : '2106751442'
    }
    return render(request, "katalog.html", context)

