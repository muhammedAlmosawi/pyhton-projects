import random
import string

def password_generator(min_length):
    characters_check = input("do you want the password to not contain characters type (n): ").lower()
    numbers_check = input("do you want the password to not contain numbers type (n): ").lower()
    has_characters = True
    has_numbers = True

    if characters_check == "n" and numbers_check == "n":
        has_characters = False
        has_numbers = False

    elif numbers_check == "n":
        has_numbers = False

    elif characters_check == "n":
        has_characters = False

    letters = string.ascii_letters
    numbers = string.digits
    characters = string.punctuation

    initial_password = letters

    if has_numbers:
        initial_password += numbers
    if has_characters:
        initial_password += characters

    final_password = ""
    meets_criteria = False
    with_numbers = False
    with_characters = False

    while not meets_criteria and len(final_password) < min_length:
        new_element = random.choice(initial_password)
        final_password += new_element

        if final_password in numbers:
            with_numbers = True
        if final_password in characters:
            with_characters = True

        meets_criteria = True

        if has_numbers:
            meets_criteria = with_numbers
        if has_characters:
            meets_criteria = meets_criteria and with_characters


    return final_password
        
    
        
