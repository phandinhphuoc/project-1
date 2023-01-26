from django.shortcuts import render
from .models import Post, tracnghiem
def home(request):
    return render(request, 'home.html', {})
def contact(request):
    return render(request, 'contact.html', {})
def login(request):
    return render(request, 'login.html', {})
def empty(request):
    return render(request, 'empty.html', {})
def toan10(request):
    return render(request, 'toan10.html', {})
def toan11(request):
    return render(request, 'toan11.html', {})
def toan12(request):
    return render(request, 'toan12.html', {})
def onthithpt(request):
    return render(request, 'onthithpt.html', {})
def tailieu(request):
    return render(request, 'tailieu.html', {})
def giaichitietdethitoanthpt2022(request):
    return render(request, 'GiaiChiTietDeThiCacNam/giaichitietdethitoanthpt2022.html', {})
def baigiang(request):
    thongtin = tracnghiem.objects.all()
    return render(request, 'Baigiang/baigiang.html', {'thongtin':thongtin})
def chuyendegiaitich12(request):
    return render(request, 'ChuyenDe/chuyendegiaitich12.html', {})