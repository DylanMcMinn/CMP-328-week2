from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Customer, engine

with Session(engine) as session:
    stmt = select(Customer).order_by(Customer.name)
    customers = session.scalars(stmt).all()

    print(f"{len(customers)} customer(s)") 
    for customer in customers:
        print(customer.id, customer.name, customer.email)