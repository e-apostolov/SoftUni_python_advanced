class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


EMAIL_MIN_LENGTH = 5
VALID_DOMAINS = ("com", "bg", "org", "net")

while True:
    input_email = input()
    if input_email == "End":
        break

    if "@" not in input_email:
        raise MustContainAtSymbolError("Email must contain @")

    if len(input_email.split("@")[0]) < EMAIL_MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    if input_email.split(".")[-1] not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")

