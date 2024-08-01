import Generator

if __name__ == "__main__":
    try:
        min_length = int(input("what is the minimum length of the password? "))
    except:
        min_length = int(input("please enter a number or the program will crash: "))
    
    password = Generator.password_generator(min_length)
    print(password)
    