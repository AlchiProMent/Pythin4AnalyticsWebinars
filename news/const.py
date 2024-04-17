from colorama import Fore, Style

_ATTENT = f'{Fore.RED}'
_NORM = f'{Fore.CYAN}'
_TXT = f'{Fore.BLUE}'
_CLEAR = f'{Style.RESET_ALL}'

_TMP_JPG = 'image_tmp.jpg'

# ключи, используемые в справочнике распарсенного текста статьи
_KEY_TITLE = 'TITLE'
_KEY_AUTOR = 'AUTOR'
_KEY_DATE = 'DATE'
_KEY_BODY = 'BODY'

_FLUKY_SITE = 0
_ny_post_com = 'nypost.com'
_NY_POST = 1
_ny_times_com = 'nytimes.com'
_NY_TIMES = 2


def site_type(url:str):
    # по URL определяет тип сайта из списка типов, возможных для парсинга
    arr = url.split('/')
    if _ny_post_com in arr[2]:
        web_site = _NY_POST
    elif _ny_times_com in arr[2]:
        web_site = _NY_TIMES
    else:
        web_site = _FLUKY_SITE
    return web_site
