import codecs
import re

from bs4 import BeautifulSoup
import requests


class Scraper:
    BASE_URL = 'https://www.imaginbank.com'
    movies = []

    def get_info(self):
        soup = self.get_soup_from_web_dummy('/descuentos/experiencias_es.html')

        for discount in soup.find_all("li", class_="descuento", limit=1):
            detail_view = self.get_detail_view(discount)
            event_info = detail_view.find(class_="informacion-bottom")
            popup_info = detail_view.find(class_="popup_informacion")

            event_info.p['class'] = 'lead'

            print(event_info.p)
            print(popup_info.find(string=re.compile("Madrid")).find_next('a').get('href'))

    def get_detail_view(self, discount):
        detail_url = discount.find(title='Ir a la oferta').get('href')
        return self.get_soup_from_web_dummy(detail_url)

    def get_soup_from_web(self, web):
        resp = requests.get(self.BASE_URL + web)
        if resp.ok:
            return BeautifulSoup(resp.text, 'html.parser')
        else:
            raise Exception('Error {code}: {msg}'.format(code=resp.status_code, msg=resp.text))

    def get_soup_from_web_dummy(self, web):
        if web == '/descuentos/experiencias_es.html':
            web_dummy = "imaginsource.html"
        else:
            web_dummy = "loganlucky.html"

        f = codecs.open(web_dummy, 'r', 'utf-8')
        return BeautifulSoup(f.read(), 'html.parser')

    def convert_to_movie(self):
        pass


scraper = Scraper()
scraper.get_info()
