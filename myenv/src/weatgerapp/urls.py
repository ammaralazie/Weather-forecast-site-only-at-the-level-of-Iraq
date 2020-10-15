from django.urls import path
from  . import views
urlpatterns=[

    path('',views.geet_city,name='geet_city')

]
