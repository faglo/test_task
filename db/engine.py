from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from os import getenv

Base = declarative_base()

# postgresql://{user}:{password}@{address}:{port}/{database}
SQLALCHEMY_DATABSE_URL = getenv("DATABASE_URL")

engine = create_engine(
    SQLALCHEMY_DATABSE_URL,
)

Session_ = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = Session_()
    try:
        yield db
    except:
        db.close()
