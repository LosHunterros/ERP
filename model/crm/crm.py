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
    users = []
    users.append(HEADERS)
    users += data_manager.read_table_from_file(file)
    return users

def add_customer(customer, file = DATAFILE):
    customer["id"] = util.generate_id()
    customer["subscribtion"] = util.convert_to_boolean(customer["subscribtion"])
    customer["email"] = customer["email"].lower()
    customer = [customer["id"], customer["name"], customer["email"], customer["subscribtion"]]
    return data_manager.append_line_to_file(file, customer)