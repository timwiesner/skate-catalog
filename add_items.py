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
session.add(category2)
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

# category10 = Category(name="T-Shirts")
# session.add(category10)
# session.commit()

# category11 = Category(name="Shoes")
# session.add(category11)
# session.commit()

item1 = Item(name="CCS Logo Skateboard Complete - Black",
             description="There’s something great in the transformation of a deck the more you skate it. Whether you draw, paint, stencil your own graphic, or let your skating create its own graphic, the CCS Logo deck only gets better with time.",
             category_id=1)
session.add(item1)
session.commit()

item2 = Item(name="Birdhouse Ben Raybourn Mexipulp Skateboard Complete - 8.25\"",
             description="Gotta look out for the killa trees!",
             category_id=1)
session.add(item2)
session.commit()

item3 = Item(name="Alien Workshop Guevara No Evil Skateboard Complete - 8.00\"",
             description="Joey gpt the pro nod!",
             category_id=1)
session.add(item3)
session.commit()



item4 = Item(name="CCS Reject Skateboard Deck",
             description="It’s hard to focus on anything but skateboarding when you’re out skating. You don’t have time to consider whether the graphic on your CCS board would be considered modernist or postmodernist.",
             category_id=2)
session.add(item4)
session.commit()

item5 = Item(name="Zero Thomas Prism Skateboard Deck - 8.25\"",
             description="For on road safety!",
             category_id=2)
session.add(item5)
session.commit()



item6 = Item(name="Rout After Hours 2 am Cruiser Skateboard Complete",
             description="This Rout Cruiser is bit like when your favorite song comes on the radio.",
             category_id=3)
session.add(item6)
session.commit()

item7 = Item(name="Landyachtz Dinghy Birds Deco Longboard Complete",
             description="The Landyachtz Dinghy is hands down one of the most fun boards we’ve ever stepped on.",
             category_id=3)
session.add(item7)
session.commit()


# session.add(item)
# session.commit()


print('Items Added!')
