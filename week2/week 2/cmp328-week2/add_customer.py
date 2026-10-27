from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import Customer, engine

name = input("Name: ").strip()
email = input ("Email:").strip().lower()

if name == "" or email == "":
    print("Name and email are both required")
else:
    with Session(engine) as session:
        try:
            session.add(Customer(name=name, email=email))
            session.commit()
            print("Customer added.")
        except IntegrityError:
            session.rollback()
            print("That email is already registered.")