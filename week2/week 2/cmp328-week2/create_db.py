from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Base, Customer, engine

Base.metadata.create_all(engine)

with Session(engine) as session:
    first= session.scalars(select(Customer)).first()
    if first is None:
        session.add_all([
            Customer(name="Ciara Brown", email="ciara@example.com"),
            Customer(name="Ben Carter", email="ben@example.com"),
            Customer(name="Chi Nakumara", email="chi@example.com"),
        ])
        session.commit()
        print("Database created with three customers")
    else:
        print("Database already has customers")