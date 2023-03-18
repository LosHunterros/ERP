""" Customer Relationship Management (CRM) module

Data table structure:
    - id (string)
    - name (string)
    - email (string)
    - subscribed (int): Is subscribed to the newsletter? 1: yes, 0: no
"""

from model import data_manager, util


DATAFILE = "model/crm/crm.csv"
HEADERS = ["id", "name", "email", "subscribed"]


def get_customers(file = DATAFILE):
    customers = []
    customers.append(HEADERS)
    customers += data_manager.read_table_from_file(file)
    return customers


def add_customer(customer, file = DATAFILE):
    customer["id"] = util.generate_id()
    customer["subscribtion"] = util.convert_to_boolean(customer["subscribtion"])
    customer["email"] = customer["email"].lower()
    customer = [customer["id"], customer["name"], customer["email"], customer["subscribtion"]]
    return data_manager.append_line_to_file(file, customer)


def edit_customer(customer, file = DATAFILE):
    customer["subscribtion"] = util.convert_to_boolean(customer["subscribtion"])
    customer["email"] = customer["email"].lower()

    customers = get_customers()
    del customers[0]

    for i in range(len(customers)):
        if customers[i][0] == customer["id"]:
            customers[i][1] = customer["name"]
            customers[i][2] = customer["email"]
            customers[i][3] = customer["subscribtion"]

    return data_manager.write_table_to_file(file, customers)


def delete_customer(id, file = DATAFILE):
    customers = get_customers()
    del customers[0]

    for i in range(len(customers)):
        if customers[i][0] == id:
            del customers[i]
            break

    return data_manager.write_table_to_file(file, customers)


def get_subscribed_emails(file = DATAFILE):
    customers = get_customers()
    customers = list(filter(lambda x: x[3] == "1", customers))
    emails = []
    for customer in customers:
        emails.append(customer[2])
    return emails


def validate_id(id):
    customers = get_customers()
    for customer in customers:
        if customer[0] == id: return id
    return False