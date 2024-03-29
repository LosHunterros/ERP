from model.crm import crm
from model import util
from view import terminal as view


def list_customers():
    customers = crm.get_customers()
    view.print_table(customers)


def add_customer():
    customer_data = get_new_customer_data()
    customer_name = customer_data["name"]
    customer_email = customer_data["email"]
    customer_subscribtion = customer_data["subscribtion"]
    if crm.add_customer({"name": customer_name, "email": customer_email, "subscribtion": customer_subscribtion}):
        view.print_message("Customer added successfully")
    else:
        view.print_error_message("Customer not added")


def update_customer():
    customer_id = view.get_input("Customer ID", crm.validate_id)
    customer_data = get_new_customer_data()
    customer_name = customer_data["name"]
    customer_email = customer_data["email"]
    customer_subscribtion = customer_data["subscribtion"]
    if crm.edit_customer({"id": customer_id, "name": customer_name, "email": customer_email, "subscribtion": customer_subscribtion}):
        view.print_message("Customer edited successfully")
    else:
        view.print_error_message("Customer not edited")


def delete_customer():
    customer_id = view.get_input("Customer ID", crm.validate_id)
    if crm.delete_customer(customer_id):
        view.print_message("Customer deleted successfully")
    else:
        view.print_error_message("Customer not deleted")


def get_subscribed_emails():
    emails = crm.get_subscribed_emails()
    view.print_general_results(emails, "Subscribed customer emails")


def get_new_customer_data():
    customer_name = view.get_input("Customer name", util.validate_text)
    customer_email = view.get_input("Customer email", util.validate_email)
    customer_subscribtion = view.get_input("Customer email subscribtion (Y - Yes ; N - No)", util.validate_boolean)

    return {"name": customer_name, "email": customer_email, "subscribtion": customer_subscribtion}


def run_operation(option):
    if option == 1:
        list_customers()
    elif option == 2:
        add_customer()
    elif option == 3:
        update_customer()
    elif option == 4:
        delete_customer()
    elif option == 5:
        get_subscribed_emails()
    elif option == 0:
        return
    else:
        raise KeyError("There is no such option.")


def display_menu():
    options = ["Back to main menu",
               "List customers",
               "Add new customer",
               "Update customer",
               "Remove customer",
               "Subscribed customer emails"]
    view.print_menu("Customer Relationship Management", options)


def menu():
    operation = None
    while operation != '0':
        display_menu()
        try:
            operation = view.get_input("Select an operation")
            run_operation(int(operation))
        except KeyError as err:
            view.print_error_message(err)
