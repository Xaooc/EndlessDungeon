from dng.database import create_db, Session
from dng.pers import Pers
from dng.users import Users
from dng.place import Place
from dng.Create_pers import GeneratorPers


def creator_db(data: bool = True):
    create_db()
    if data:
        _data(Session())

def _data(session: Session):
    pass