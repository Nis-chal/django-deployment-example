from django.urls import path

from urlapp import views

app_name = 'urlapp'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),

]
