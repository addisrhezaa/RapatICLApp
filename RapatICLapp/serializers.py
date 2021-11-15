from rest_framework import serializers
from RapatICLapp.models import Notulensi, Rapat, Absensi, Asisten

class AsistenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Asisten
        fields = "__all__"

class AbsensiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Absensi
        depth = 1
        fields = ['asisten', 'rapat', 'hadir']

class AbsensiPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Absensi
        fields = ['asisten', 'rapat', 'hadir']

class RapatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rapat
        fields = ['topik', 'tanggal']

class NotulensiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notulensi
        fields = ['rapat','konten','notulen']    

class DetailSerializer(serializers.Serializer):
    topik = serializers.CharField()
    tanggal = serializers.CharField()
    kehadiran = AbsensiSerializer(many = True)

class DetailAsisten(serializers.Serializer):
    asisten = AsistenSerializer()
    total_rapat = serializers.IntegerField()
    total_hadir = serializers.IntegerField()
    total_absen = serializers.IntegerField()