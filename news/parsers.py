# парсеры для разных сайтов

from bs4 import BeautifulSoup
from bs4.element import Tag as bs4Tag
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager

from const import _KEY_TITLE, _KEY_AUTOR, _KEY_DATE, _KEY_BODY
from funcs import *


def nytimes_art_parser(art_url):
    # создать объект для настройки опций
    options = Options()
    # установить стратегию загрузки
    options.page_load_strategy = 'normal'
    # не показывать браузер Chrome
    options.headless = True

    # создать драйвер
    msg('Эмуляция браузера')
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    full_art = {}

    # загрузить страницу
    try:
        driver.get(art_url)
    except Exception as e:
        err_msg('Ошибка загрузки')
        print(e)
    else:

        # прокрутить страницу вниз
        try:
            driver.execute_script("window.scrollTo(0,document.body.clientHeight);")
        except Exception as e:
            err_msg('Ошибка прокрутки')
            print(e)
        else:
            msg('Ok')

            title = driver.find_element(by=By.TAG_NAME, value='h1')
            full_art[_KEY_TITLE] = title.text
            # получить автора
            autor = driver.find_element(by=By.CLASS_NAME, value='last-byline')
            full_art[_KEY_AUTOR] = autor.text
            # получить дату публикации
            art_date = driver.find_element(by=By.TAG_NAME, value='time')
            full_art[_KEY_DATE] = art_date.get_attribute('datetime')

            art_content = []
            try:
                summary = driver.find_element(by=By.ID, value='article-summary')
            except:
                pass
            else:
                # print(summary.text)
                # print()
                art_content.append({'h4': summary.text})

            try:
                # получить весь текст статьи
                art_body = driver.find_element(by=By.CLASS_NAME, value='meteredContent')
            except:
                pass
            else:
                divs = art_body.find_elements(by=By.TAG_NAME, value='div')
                last_scr = ''
                for ind, div in enumerate(divs):
                    paragraphs = div.find_elements(by=By.TAG_NAME, value='p')
                    if paragraphs:
                        last_scr = ''
                        attr = div.get_attribute('class')
                        if attr == 'css-s99gbd StoryBodyCompanionColumn':
                            for p in paragraphs:
                                attr = p.get_attribute('class')
                                if attr == 'css-at9mc1 evys1bk0':
                                    art_content.append({'p': p.text})
                                else:
                                    art_content.append({'h5': p.text})
                    else:
                        try:
                            picture = div.find_element(by=By.TAG_NAME, value='img')
                        except:
                            pass
                        else:
                            src = picture.get_attribute('src')
                            img_srcset = picture.get_attribute('srcset')
                            if src != last_scr:
                                # print(src)
                                figure = {'src': src}
                                lst_srcset = []
                                last_scr = src
                                try:
                                    img_text = div.find_elements(by=By.TAG_NAME, value='figcaption')
                                except:
                                    pass
                                else:
                                    if len(img_text) > 0:
                                        s = img_text[0].text
                                        s = s.replace('Credit...', '')
                                        figure['figure'] = s

                                if img_srcset:
                                    # порубить его на куски по границе ширины изображений
                                    srcsets = str(img_srcset).split('w,')
                                    # убрать литеру w в последней строке
                                    srcsets[-1] = srcsets[-1][:-1]
                                    # сформировать массив значений
                                    for srcset in srcsets:
                                        s = srcset.split()
                                        # добавить значения из списка дополнительных src
                                        try:
                                            # получить ширину картинки
                                            width = int(s[1])
                                        except:
                                            width = -1
                                        else:
                                            # Добавить только если ширина картинки представляет из себя целое число
                                            lst_srcset.append([s[0], width])

                                print()
                                if len(lst_srcset) > 0:
                                    figure['srcset'] = lst_srcset
                                # добавить в ссписок элемиентов, из которого состоит статья
                                art_content.append(figure)

            full_art[_KEY_BODY] = art_content

            driver.close()

    return full_art


def nypost_art_parser(dom:BeautifulSoup):
    # парсинг статьи New York Post на основе DOM
    full_art = {}

    # получить заголовок
    title = dom.find('h1')
    full_art[_KEY_TITLE] = title.text.strip()

    # получить автора
    autor = dom.find(id='author-flyout-label')
    # криво, но по другому не получается из-за странной конструкции блока с именем автора
    if autor:
        for a in autor:
            s = a
        full_art[_KEY_AUTOR] = s.replace('\n\t', '').strip()

    # получить дату публикации
    art_date = dom.find('div', class_='date--updated__item').findAll('span')[1]
    full_art[_KEY_DATE] = art_date.text

    # получить весь текст статьи
    art_body = dom.find('div', class_='single__content')
    # теги, которые представляют интерес
    needed_tags = ['p', 'h2', 'figure']
    art_content = []
    # перебрать все элементы строки
    for element in art_body:
        # получить имя тега
        tag = element.name
        if tag in needed_tags:
            if tag != 'figure':
                art_content.append({tag: element.text})
            else:
                # если это описание картинки, надо с ней поработать отдельно
                s = element.text
                # в начале строки идёт несколько ненужных символов, указывающих количество фотографий в тексте вида \n\n12\n\n
                s = re.sub(r'^\n{2}\d+\n{2}', '', s)
                figure = {tag: s}
                img_src = None
                lst_srcset = []

                img = element.find('img')
                # если это HTML-тег доппустимого класса
                if isinstance(img, bs4Tag):
                    # ссылка на основное фото
                    img_src = img.get('src')
                    # ссылка на дополнительный сет
                    img_srcset = img.get('srcset')
                    # если дополнительный сет имеется
                    if img_srcset:
                        # порубить его на куски по границе ширины изображений
                        srcsets = str(img_srcset).split('w,')
                        # убрать литеру w в последней строке
                        srcsets[-1] = srcsets[-1][:-1]
                        # сформировать массив значений
                        for srcset in srcsets:
                            s = srcset.split()
                            # добавить значения из списка дополнительных src
                            try:
                                # получить ширину картинки
                                width = int(s[1])
                            except:
                                width = -1
                            else:
                                # Добавить только если ширина картинки представляет из себя целое число
                                lst_srcset.append([s[0], width])

                if img_src:
                    figure['src'] = img_src
                if len(lst_srcset) > 0:
                    figure['srcset'] = lst_srcset
                # добавить в список элементов, из которого состоит статья
                art_content.append(figure)

    # добавить в общий справочник
    full_art[_KEY_BODY] = art_content

    return full_art