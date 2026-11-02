from django.urls import path
from . import views
urlpatterns=[
    path('getbookings/',views.getbookinginfo,name="getbookings")
]