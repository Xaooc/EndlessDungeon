import os

from dng.database import Pers, Users, Place, DATABASE_NAME, Session, create_db


if __name__ == "__main__":
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        create_db()


