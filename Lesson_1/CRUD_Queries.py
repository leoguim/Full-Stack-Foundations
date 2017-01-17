### Before we perform any operations, we must first import the necessary 
### libraries, connect to our restaurantMenu.db, and 
### create a session to interface with the database:

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantMenu.db')
Base.metadata.bind=engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

### CREATE
### We created a new Restaurant and called it Pizza Palace:

cheesepizza = menuItem(name="Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course="Entree", price="$8.99", restaurant=myFirstRestaurant)
session.add(cheesepizza)
session.commit()

### We created a cheese pizza menu item and added it to the Pizza Palace Menu:

items = session.query(MenuItem).all()
for item in items:
    print item.name

### UPDATE
### We found the veggie burger that belonged to the Urban Burger 
### restaurant by executing the following query:

veggieBurgers = session.query(MenuItem).filter_by(name= 'Veggie Burger')
for veggieBurger in veggieBurgers:
    print veggieBurger.id
    print veggieBurger.price
    print veggieBurger.restaurant.name
    print "\n"

UrbanVeggieBurger = session.query(MenuItem).filter_by(id=8).one()
UrbanVeggieBurger.price = '$2.99'
session.add(UrbanVeggieBurger)
session.commit() 

### DELETE

### We deleted spinach Ice Cream from our Menu Items 
### database with the following operations:

spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
session.delete(spinach)
session.commit() 