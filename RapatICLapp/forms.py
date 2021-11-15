from django import forms
from .models import Absensi, Notulensi, Rapat

class PostRapat(forms.ModelForm):
    class Meta:
        model = Rapat
        fields = ['topik', 'tanggal']

class PostNotulensi(forms.ModelForm):
    class Meta:
        model = Notulensi
        fields = ['rapat','konten','notulen']

class PostAbsensi(forms.ModelForm):
    class Meta:
        model = Absensi
        fields = ['asisten', 'rapat', 'hadir']