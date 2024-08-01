from main import *


def view():
    with open("password_manager/passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            name, password= data.split("|")
            print("user:", name, '\t', "password:", fer.decrypt(password))


def add():
    name = input("what is your username: ")
    password = input("please enter the new password: ")

    with open("password_manager/passwords.txt", 'a') as f:
        f.write(name + "\t | \t" + fer.encrypt(password.encode()).decode() + "\n")