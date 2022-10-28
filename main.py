import os

from sqlalchemy import and_

from dng.pers import Pers
from dng.users import Users
from dng.place import Place

from dng.database import DATABASE_NAME, Session
import dng.creator_db as db_cr


if __name__ == "__main__":
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_cr.create_db()


