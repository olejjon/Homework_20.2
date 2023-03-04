from unittest.mock import MagicMock
import pytest

from dao.director import DirectorDAO
from dao.model.director import Director
from service.director import DirectorService
from setup_db import db


# тесты
@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    jonh = Director(id=1, name='jonh')
    kate = Director(id=2, name='kate')
    max = Director(id=3, name='max')

    director_dao.get_one = MagicMock(return_value=jonh)
    director_dao.get_all = MagicMock(return_value=[jonh, kate, max])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_create(self):
        director_d = {
            "name": "Ivan",
            "age": 39,
        }
        director = self.director_service.create(director_d)
        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_d = {
            "id": 3,
            "name": "Ivan",
            "age": 39,
        }
        self.director_service.update(director_d)

# реальный класс


# class DirectorService:
#     def __init__(self, dao: DirectorDAO):
#         self.dao = dao
#
#     def get_one(self, bid):
#         return self.dao.get_one(bid)
#
#     def get_all(self):
#         return self.dao.get_all()
#
#     def create(self, director_d):
#         return self.dao.create(director_d)
#
#     def update(self, director_d):
#         return self.dao.update(director_d)
#
#     def partially_update(self, director_d):
#         director = self.get_one(director_d["id"])
#         if "name" in director_d:
#             director.name = director_d.get("name")
#         self.dao.update(director)
#
#     def delete(self, rid):
#         self.dao.delete(rid)