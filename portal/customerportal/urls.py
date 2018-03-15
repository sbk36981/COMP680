from django.conf.urls import url
from django.urls import path

from . import views
app_name = 'cusportal'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('<int:house_id>/', views.housedetail, name="housedetail"),
    path('<int:house_id>/prediction', views.prediction, name="prediction")
]
