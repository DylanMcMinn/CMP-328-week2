from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models import Customer, engine

customer_id = int(input("Customer id: "))

with Session(engine) as session:
    customer = session.get(Customer, customer_id)

    if customer is None:
        print("No customer with that id.")
    else:
        print("Current email:", customer.email)
        customer.email = input("New email: ").strip().lower()
        try:
            session.commit()
            print("Email updated. ")
        except IntegrityError:
            session.rollback()
            print("That email is already used by another customer.")
        