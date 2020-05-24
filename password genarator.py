import random
import string

special_char = ("$", "#", ".", "!")
name=input("enter your name")
print(f"Hello {name}")
while True:
    try:
        user = int(input("enter length of password b/w 6 to 16"))
        if user >= 6 and user <= 16:
            password = user
        elif user <= 6:
            print("password cant be less than 6 character")
            continue
        elif user >= 18:
            print("password cant be more than 18 character")
            continue

        alphabets = int(input("enter number of alphabets"))
        numbers = int(input("enter num of numbers"))
        symbols = int(input("enter num of symbols"))
        password_length=alphabets+numbers+symbols
        if user==password_length:
            password = ""
            for i in range(alphabets):
                pass1 = random.choice(string.ascii_letters)
                password += pass1
            for i in range(numbers):
                pass2 = random.choice(string.digits)
                password += pass2
            for i in range(symbols):
                pass3 = random.choice(special_char)
                password += pass3
            print(password, end="")
            pass_list = list(password)
            random.shuffle(pass_list)
            finalpassword = ''.join(pass_list)
            print("\nshuffled password is: ", finalpassword)
            ask1=input("do you want this generated password y for yes n for no" )
            if ask1=="n":
                continue
            else:
                print("thanks for selecting this password")
                break
        else:
            print("please take proper sum of input which is equal to length of password" )
    except ValueError as error:
        print("please enter valid input must be in number format")
        print(error)