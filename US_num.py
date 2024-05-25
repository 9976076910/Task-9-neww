import re


# function for Validating Phone number
def val_phone_number(regex, phone_number):
    match = re.search(regex, phone_number)
    if match:
        return True
    return False


#  regular expression and complie method
pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")

test_phone_number = [
    "+1-325-1234-5678"

]

for number in test_phone_number:
    print(f"{number}: {val_phone_number(pattern, number)}")