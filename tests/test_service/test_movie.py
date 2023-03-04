from unittest.mock import MagicMock
import pytest

from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService
from setup_db import db


# тесты
@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    movie1 = Movie(id=1, title='aas', description='asdddd', trailer='ososos', year=2021, rating=2.2, genre_id=1,
                   director_id=1)
    movie2 = Movie(id=2, title='asdasdasd', description='222', trailer='3333232', year=2022, rating=2.1, genre_id=2,
                   director_id=2)
    movie3 = Movie(id=3, title='asdasd', description='asd222ddd', trailer='32', year=2023, rating=2.3, genre_id=3,
                   director_id=3)

    movie_dao.get_one = MagicMock(return_value=movie1)
    movie_dao.get_all = MagicMock(return_value=[movie1, movie2, movie3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_d = {
            "title": "aas",
        }
        movie = self.movie_service.create(movie_d)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_d = {
            "id": 1,
            "title": "aas"
        }
        self.movie_service.update(movie_d)
