from django.urls import path
from crudapp.views import *

urlpatterns = [
   path('', data_add, name='add'),
   path('view', data_view, name='view'),
   path('update/<id>', data_update, name='update'),
   path('delete', data_delete, name='delete'),
]