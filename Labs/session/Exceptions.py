class ContactNotFoundException(Exception):
    def __init__(self, message="Cannot login !") -> None:
        print(message)

class ContactAlreadyExistsException(Exception):
    pass

class DBException(Exception):
    pass