"""Définit la bibliothèque virtuelle."""

import random

from .film import FilmCleaner
from .data import films


class Library:
    """Bibliothèque de films."""

    def __init__(self):
        """Initialise les films."""
        self.films = []
        for film_data in films:
            film = FilmCleaner(film_data).generate()
            film.where = self
            self.films.append(film)

        self.sort_by_date_and_name()

    def sort_by_date_and_name(self):
        """Tri les films par date et par nom."""
        self.films.sort(key=lambda film: (film.date, film.name))

    def sort_by_type(self):
        """Tri les films par type."""
        self.films.sort(key=lambda film: film.type)

    def get_random_choice(self):
        """Retourne un film au hasard."""
        return random.choice(self.films)

    def get_films_lent(self):
        """retourne la liste des films prêtés.

        Note: j'utilise ici une liste de compréhension. Renseignez vous
        sur son utilisation si vous ne savez pas les utiliser
        """
        return [film for film in self.films if film.where is not self]

    def find_by_name(self, name):
        """Retourne un film si le nom correspond, sinon None."""
        for film in self.films:
            if name == film.name:
                return film
        return None
