from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Base, Category, Item

engine = create_ending('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession
