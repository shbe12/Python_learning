registered_users = []
failed_registrations = []

def validate_name(name):
    if len(name) >= 3:
        return True
    else:
        return False


def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False



def validate_password(password):
    if len(password) >= 8:
    if any(c.isupper() for c in password):
    if any(c.isdigit() for c in password):

    else:
        return False

def validate_password(password):
    return(
        len(password)>=8
        and any(c.isupper() for c in password)
        and any(c.isdigit() for c in password)
    )
