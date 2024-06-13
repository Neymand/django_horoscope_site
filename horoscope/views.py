from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - <i>пятый знак зодиака</i>, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',}

zodiac_element = {'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']}

zodiac_dates = {1:  {'capricorn': (1, 20),   'aquarius': (21, 31)},
    2:  {'aquarius': (1, 19),    'pisces': (20, 29)},
    3:  {'pisces': (1, 20),      'aries': (21, 31)},
    4:  {'aries': (1, 20),       'taurus': (21, 30)},
    5:  {'taurus': (1, 21),      'gemini': (22, 31)},
    6:  {'gemini':  (1, 21),     'cancer': (22, 30)},
    7:  {'cancer':  (1, 22),     'leo': (23, 31)},
    8:  {'leo': (1, 21),         'virgo': (22, 31)},
    9:  {'virgo': (1, 22),       'libra': (23, 30)},
    10: {'libra': (1, 23),       'scorpio': (24, 31)},
    11: {'scorpio': (1, 22),     'sagittarius': (23, 30)},
    12: {'sagittarius': (1, 22), 'capricorn': (23, 31)}}

def check_date(requests, month, day):
    check = zodiac_dates[month]
    for key, value in check.items():
        if value[0] <= day and value[1] >= day:
            redirect_path = reverse('horoscope-name', args=(key,))
            return HttpResponseRedirect(redirect_path)

def get_element(requests):
    element_list = list(zodiac_element)
    element_menu = ''
    for sing in element_list:
        redirect_path = reverse('horoscope-type', args=[sing])
        element_menu += f"<li> <a href='{redirect_path}'>{sing.title()}</li>"
    return HttpResponse(element_menu)

def menu_sort_element(requests, element: str):
    element_list = zodiac_element[element]
    element_menu = ''
    for sing in element_list:
        redirect_path = reverse('horoscope-name', args=[sing])
        element_menu += f"<li> <a href='{redirect_path}'>{sing.title()}</li>"
    return HttpResponse(element_menu)


def index(requests):
    # f"<li> <a href='{redirect_path}'>{sing.title()}</li>"
    zodiac_list = list(zodiac_dict)
    context = {
        'zodiacs': zodiac_list
    }
    return render(requests, 'horoscope/index.html', context=context)

def get_info_about_zodiac(requests, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, None)
    zodiacs = list(zodiac_dict)
    data = {
        'description_zodiac': description,
        'sign': sign_zodiac,
        'sign_name': description.split()[0],
        'zodiacs': zodiacs
    }
    if description:
        return render(requests, 'horoscope/info_zodiac.html', context=data)
    else:
        return HttpResponseNotFound('Пук-среньк')

def get_info_about_zodiac_by_number(requests, sign_zodiac: int):
    zodiac_list = list(zodiac_dict)
    if sign_zodiac > len(zodiac_list):
        return HttpResponseNotFound(f'Нет знака зодиака под номером {sign_zodiac}')
    else:
        name_zodiac = zodiac_list[sign_zodiac-1]
        redirect = reverse('horoscope-name', args=(name_zodiac,))
        return HttpResponseRedirect(redirect)