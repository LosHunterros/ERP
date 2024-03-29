def print_menu(title, list_options):
    """Prints options in standard menu format like this:

    Main menu:
    (1) Store manager
    (2) Human resources manager
    (3) Inventory manager
    (0) Exit program

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(f"\n{title.upper()}\n")
    for i, option in enumerate(list_options):
        print(f"({i}) {option}")


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(f"\nMessage: {message}")


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if isinstance(result, list):
        print(f"\n{label.upper()}: \n")
        for item in result:
            print(f"{item}; ", end="")
        print("")


# /--------------------------------\
# |   id   |   product  |   type   |
# |--------|------------|----------|
# |   0    |  Bazooka   | portable |
# |--------|------------|----------|
# |   1    | Sidewinder | missile  |
# \-----------------------------------/
def print_table(table):
    """Prints tabular data like above.

    Args:
        table: list of lists - the table to print out
    """
    first_line = True
    for i in range(len(table[0])): table[0][i] = table[0][i].upper()
    print("\n/-----------------------------------------------------------------------------------------------------------------------------------\\")
    for row in table:
        if not first_line: print("|-----------------------------------------------------------------------------------------------------------------------------------|")
        for col in row:
            print(f"| {col.ljust(30)} ", end="")
        print("|")
        first_line = False
    print("\\-----------------------------------------------------------------------------------------------------------------------------------/")


def get_input(label, validate=False):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    user_input = False

    while not user_input:
        user_input = input(f"\n{label}: ")
        if validate: user_input = validate(user_input)
        if not user_input: print_error_message(f"{label}. Please try again")

    return user_input


def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    pass


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(f"\nERROR: {message}")
