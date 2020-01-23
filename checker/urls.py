from django.urls import path
from .views import *


app_name = 'checker'

urlpatterns = [
    path('', checker_page, name='checker_page_url'),
    path('<int:pk>/update/', CheckerUpdate.as_view(), name='checker_update_url'),
    path('create/', CheckerCreate.as_view(), name='checker_create_url'),
    path('create/link/', LinkCreate.as_view(), name='link_create_url'),
]
