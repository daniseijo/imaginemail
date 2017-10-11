from tmdb import TMDBInfo


class Movie:
    def __init__(self, title, image, extra_info, link):
        self.title = title
        self.image = image
        self.extra_info = extra_info
        self.purchase_link = link

        self._get_tmdb_info()

    def _get_tmdb_info(self):
        info = TMDBInfo(title=self.title)

        self.title = info.get_title()
        self.overview = info.get_overview()
        self.image = info.get_image()
