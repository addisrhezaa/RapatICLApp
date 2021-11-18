import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import PostRapat, PostAbsensi, PostNotulensi
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from RapatICLapp.models import Notulensi, Rapat, Absensi, Asisten
from RapatICLapp.serializers import (AsistenSerializer,
 AbsensiSerializer, 
 DetailSerializer, NotulensiSerializer, 
 RapatSerializer,
 DetailAsisten,
 AbsensiPostSerializer)

# Create your views here.
def homepage(request):
    asisten = Asisten.objects.all()
    listtotal = []
    for item in asisten:
        temp = {}
        nim = item.nim
        temp['nim'] = item.nim
        temp['nama'] = item.nama
        total_hadir = len(Absensi.objects.filter(asisten__nim=nim).filter(hadir = True))
        temp['total_hadir'] = total_hadir
        listtotal.append(temp)
    total_rapat = len(Rapat.objects.all())
    data = {'nama' : listtotal, 'total_rapat': total_rapat}
    print(asisten)
    return render(request,'index.html',data)

class asisten_list(APIView):
    def get(self, request):
        asisten = Asisten.objects.all()
        serializer = AsistenSerializer(instance = asisten, many = True)
        return Response(serializer.data)
  
class rapat_list(APIView):

    def get(self, request):
        rapat = Rapat.objects.all()
        serializer = RapatSerializer(instance=rapat, many=True)
        return Response(serializer.data)

    def post(self, request):
        print(request.data)
        rapat_id = 0
        rapat_serializer = RapatSerializer(data = request.data['rapat'])

        if rapat_serializer.is_valid():
            rapat_new = rapat_serializer.save()
            rapat_id = rapat_new.id
            absensi = request.data['absensi']
            absensi_list = []

        all_asisten = Asisten.objects.all()

        for asisten in all_asisten:
            print(asisten)
            absensi_obj = {}
            absensi_obj["asisten"] = asisten.nim
            if asisten.nim in absensi:
                absensi_obj["hadir"] = False
            else:
                print(asisten.nim)
                absensi_obj["hadir"] = True
            absensi_obj["rapat"] = rapat_id
            absensi_list.append(absensi_obj)
        
        absensi_serializer = AbsensiPostSerializer(data = absensi_list, many = True)
        if absensi_serializer.is_valid():
            print("VALID")
            print(absensi_serializer.data)
            absensi_serializer.save()

        return Response({"status":"success"})

class notulensi_list(APIView):

    def get(self, request):
        notulensi = Notulensi.objects.all()
        serializer = NotulensiSerializer(instance=notulensi, many=True)
        return Response(serializer.data)

class absensi_list(APIView):

    def get(self, request):
        absensi = Absensi.objects.all()
        serializer = AbsensiSerializer(instance=absensi, many = True)
        return Response(serializer.data)
  
class hadir_list(APIView):

    def get(self, request, pk):
        data = {}

        rapat = Rapat.objects.get(pk = pk)
        absensi = Absensi.objects.filter(rapat__rapat=pk).filter(hadir = True)
        
        data["topik"] = rapat.topik
        data['tanggal'] = rapat.tanggal
        data['kehadiran'] = absensi
        serializer = DetailSerializer(data)
        return Response(data = serializer.data)

class tidak_hadir_list(APIView):
    def get(self, request, pk):
        data = {}

        rapat = Rapat.objects.get(pk = pk)
        absensi = Absensi.objects.filter(rapat__rapat=pk).filter(hadir = False)
        
        data["topik"] = rapat.topik
        data['tanggal'] = rapat.tanggal
        data['kehadiran'] = absensi
        serializer = DetailSerializer(data)
        return Response(data = serializer.data)

class detail_asisten(APIView):
    def get(self, request, nim):
        data = {}
        total_rapat = len(Rapat.objects.all())
        total_hadir = len(Absensi.objects.filter(asisten__nim=nim).filter(hadir = True))
        print(total_hadir)
        total_absen = total_rapat - total_hadir
        asisten = Asisten.objects.get(nim = nim)
        data['asisten'] = asisten
        data['total_hadir'] = total_hadir
        data['total_rapat'] = total_rapat
        data['total_absen'] = total_absen

        serializer = DetailAsisten(data)
        return Response(data = serializer.data)