from sqlalchemy import select
from sqlalchemy.orm import Session
from models import Customer, engine


def list_customers(session):
    stmt = select(Customer).order_by(Customer.name)
    for customer in session.scalars(stmt):
        print(customer.id, customer.name, customer.email)


with Session(engine) as session:
    while True:
        print("1 = list customers, 2 = quit")
        choice = input("Choice: ").strip()
        if choice == "1":
            list_customers(session)
        elif choice == "2":
            break
        else:
            print("Please type 1 or 2. ")