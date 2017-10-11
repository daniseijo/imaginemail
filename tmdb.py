import requests
import os
import json


class TMDBInfo:
    BASE_URL = 'https://api.themoviedb.org/3/search/movie'

    def __init__(self, title):
        self.movie_json = self.search_film(title)

    def search_film(self, title):
        api_key = os.environ.get('API_KEY')
        resp = requests.get(
            self.BASE_URL + '?language={lang}&api_key={api_key}&query={query}'.format(
                lang='es-ES',
                api_key=api_key,
                query=title
            )
        )

        if resp.ok:
            load = json.loads(resp.text)
            total = load.get('total_results')
            if total == 0:
                raise Exception('No results')
            results = load.get('results')
            return results[0]
        else:
            raise Exception('Error {code}: {msg}'.format(code=resp.status_code, msg=resp.text))

    def _get_from_json(self, data):
        return self.movie_json.get(data)

    def get_title(self):
        return self._get_from_json('title')

    def get_overview(self):
        return self._get_from_json('overview')
