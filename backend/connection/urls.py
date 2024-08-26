from django.urls import path
from . import views

app_name='connection'

urlpatterns=[
    path('',views.inbox,name='inbox'),
    path('',views.detail,name='detail'),
    path('new/<int:item_pk>/',views.new_connection,name='new_connection'),
]