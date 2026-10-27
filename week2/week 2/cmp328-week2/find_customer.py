from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Customer, engine

email = input("Email to find: ").strip().lower()

with Session(engine) as session:
    stmt = select(Customer).where(Customer.email == email)
    customer = session.scalars(stmt).first()

    if customer is None:
        print("No customer has that email.")
    else:
        print(customer.id, customer.name, customer.phone)