from sqlalchemy.orm import Session
from models import Customer, engine

customer_id = int(input("Customer, customer_id: "))

with Session(engine) as session:
    customer = session.get(Customer, customer_id)

    if customer is None:
        print("No Customer with that id.")
    else:
        answer = input(f"Delete {customer.name}? Type yes: ")
        if answer == "yes":
            session.delete(customer)
            session.commit()
            print("Customer deleted.")
        else:
            print("Nothing deleted.")