from cryptography.fernet import Fernet
import modes

'''
def key_file():
    key = Fernet.generate_key()
    with open("key.key", "wb") as file:
        file.write(key)
'''
def load_key():
    with open("password manager/key.key", "rb") as file:
        key = file.read()
    return key


key = load_key() + "pass".encode()
fer = Fernet(key)

if __name__ == "__main__":
    password_entered = input("please enter the master password: ")
    while password_entered != "pass":
        password_entered = input("please enter the correct master password: ")
    while (True):
        mode = input("do you want to view an existing password or add a new one type (view) or (add) type (Q) to quit: ").lower()
        if mode == "q":
            break

        elif mode == "add":
            modes.add()

        elif mode == "view":
            modes.view()

        else:
            print("please choose one of the three options")
