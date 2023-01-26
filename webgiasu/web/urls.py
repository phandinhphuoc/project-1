from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('login.html', views.login, name="login"),
    path('toan10.html', views.toan10, name="toan10"),
    path('toan11.html', views.toan11, name="toan11"),
    path('toan12.html', views.toan12, name="toan12"),
    path('onthithpt.html', views.onthithpt, name="onthithpt"),
    path('giaichitietdethitoanthpt2022.html', views.giaichitietdethitoanthpt2022, name="giaichitietdethitoanthpt2022"),
    path('baigiang.html', views.baigiang, name="baigiang"),

    path('empty.html', views.empty, name="empty"),
    path('tailieu.html', views.tailieu, name="tailieu"), 
    path('chuyendegiaitich12.html', views.chuyendegiaitich12, name="chuyendegiaitich12"), 
]
