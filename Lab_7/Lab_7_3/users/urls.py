from django.urls import path
from . import views


urlpatterns = [
    path('', views.get_filter, name='filter_choice'),
    path('search_by_name', views.get_name, name='user_name'),
    path('search_by_name/results', views.user_by_name, name='user_by_name'),
    path('search_by_date', views.get_date, name='user_date'),
    path('search_by_date/results', views.user_by_date, name='user_by_date'),
]


#urlpatterns = [
#    path('', views.get_name, name='user_name'),
#    path('user/search_by_name', views.user_by_name, name='user_by_name'),
#    path('', views.get_date, name='user_date'),
#    path('user/search_by_date', views.user_by_date, name='user_by_date'),
#]