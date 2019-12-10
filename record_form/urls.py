from django.urls import path
from record_form import views
# from django.contrib.auth import views as auth_views
from . views import Home, PersonInfoCreate, PersonInfoList, PersonInfoDetail, PersonInfoUpdate

app_name = 'record_form'
urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('create/new/', PersonInfoCreate.as_view(), name='create_person'),
    path('all/records/', PersonInfoList.as_view(), name='all_records'),
    path('record_details/<int:pk>/',
         PersonInfoDetail.as_view(), name='record_detail'),
    path('update_record/<int:pk>/',
         PersonInfoUpdate.as_view(), name='update_record'),
]
