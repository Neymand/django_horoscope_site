from django.urls import path
from . import views as views_horoscope

urlpatterns = [
    path('', views_horoscope.index),
    path('type/', views_horoscope.get_element),
    path('<int:month>/<int:day>', views_horoscope.check_date),
    path('type/<str:element>/', views_horoscope.menu_sort_element, name='horoscope-type'),
    path('<int:sign_zodiac>/', views_horoscope.get_info_about_zodiac_by_number),
    path('<str:sign_zodiac>/', views_horoscope.get_info_about_zodiac, name='horoscope-name'),


]