import os

from connection import Connection
from notification import EmailNotification
from tmdb import TMDBInfo


class Movie:
    def __init__(self, title, image, extra_info, link):
        self.title = title
        self.image = image
        self.extra_info = extra_info
        self.purchase_link = link

        self.db_name = os.environ.get('DB_NAME')
        # self._get_tmdb_info()

    def register_movie_on_db(self):
        with Connection(self.db_name) as conn:
            conn.insert_movie(self)

    def notify_to_email(self):
        movies = []
        with Connection(self.db_name) as conn:
            query = conn.get_not_notified_movies()
            for row in query:
                m = Movie(row[1], row[2], row[3], row[4])
                movies.append(m)

        en = EmailNotification()

        en.send_email('danisanse1991@gmail.com', movies)

    def _get_tmdb_info(self):
        info = TMDBInfo(title=self.title)

        self.title = info.get_title()
        self.overview = info.get_overview()
        self.image = info.get_image()


if __name__ == '__main__':
    movie = Movie('Logan4',
                  '/deployedfiles/imaginbank/Estaticos/Imagenes/Experiencias/la_suerte_de_los_logan_610x450_preestreno_es.jpg',
                  'Los logan son muy pardos',
                  '/deployedfiles/imaginbank/Estaticos/Imagenes/Experiencias/la_suerte_de_los_logan_610x450_preestreno_es.jpg')

    movie.notify_to_email()
