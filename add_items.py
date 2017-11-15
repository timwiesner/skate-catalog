from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db_setup import Base, Category, Item


engine = create_engine('sqlite:///skatecatalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


category1 = Category(name="Complete Skateboards")
session.add(category1)
session.commit()

category2 = Category(name="Skateboard Decks")
session.add(category1)
session.commit()

category3 = Category(name="Cruisers")
session.add(category3)
session.commit()

category4 = Category(name="Skate Wheels")
session.add(category4)
session.commit()

category5 = Category(name="Skate Trucks")
session.add(category5)
session.commit()

category6 = Category(name="Bearings")
session.add(category6)
session.commit()

category7 = Category(name="Helmets")
session.add(category7)
session.commit()

category8 = Category(name="Griptape")
session.add(category8)
session.commit()

category9 = Category(name="Stickers")
session.add(category9)
session.commit()

print('Items Added!')

# category10 = Category(name="T-Shirts")
# session.add(category10)
# session.commit()

# category11 = Category(name="Shoes")
# session.add(category11)
# session.commit()
