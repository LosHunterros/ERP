import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):

    length = number_of_small_letters + number_of_capital_letters + number_of_digits + number_of_special_chars
    id = list(range(length))
    random_positions = []

    while len(random_positions) < length:
        random_number = random.randint(0,length-1)
        if random_number not in random_positions: random_positions.append(random_number)

    for i in range(number_of_small_letters):
        id[random_positions[0]] = random.choice(string.ascii_lowercase)
        del random_positions[0]
    for i in range(number_of_capital_letters):
        id[random_positions[0]] = random.choice(string.ascii_uppercase)
        del random_positions[0]
    for i in range(number_of_digits):
        id[random_positions[0]] = random.choice(string.digits)
        del random_positions[0]
    for i in range(number_of_special_chars):
        id[random_positions[0]] = random.choice(allowed_special_chars)
        del random_positions[0]

    return "".join(id)


def convert_to_boolean(data):
    if data == "y": return "1"
    elif data == "n": return "0"
    else: return False


def validate_text(text):
    if len(text) < 1 or len(text) > 30: return False
    return text


def validate_email(email):
    try:
        email_splitted = email.split("@")
        email_user = email_splitted[0]
        email_user_splitted = email_user.split(".")
        email_domain = email_splitted[1]
        email_domain_splitted = email_domain.split(".")

        accepted_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "-" + "."

        if len(email) < 1 or len(email) > 30: return False
        if len(email_splitted) != 2: return False

        if len(email_domain_splitted) < 2: return False
        if len(email_domain_splitted[-1]) < 2: return False

        for char in email_user:
            if char not in accepted_chars: return False
        for char in email_domain:
            if char not in accepted_chars: return False

        for fragment in email_domain_splitted:
            if fragment[0] == "-": return False
            if fragment[-1] == "-": return False

        for fragment in email_user_splitted:
            if fragment[0] == "-": return False
            if fragment[-1] == "-": return False

        if ".." in email: return False

    except:
        return False

    return email


def validate_boolean(text):
    if text.lower() != "y" and text.lower() != "n": return False
    return text.lower()