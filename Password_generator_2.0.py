# Hello! It's Godwin again. This is a slightly detailed verion of my password generator project.
# The key diffence is that I've traded to ability to create multiple passwords at once for being able to specify how many uppercase or lowercase letters or symbols the password should include.
# I thought having this feature would be nice for people who are required to meet specific requirements.
# I imported shuffle because the password was coming out in a specific pattern depending on the numbers given in the preferences
# for example, a preference of 3lowercases, 3uppercases, and 3symbols would come out as "ahbDPN&(!" and I felt like having a predictable pattern would defeat the purpose.
# Hope you enjoy it!!


import random
from random import shuffle


lowercase  = "abcdefghijklmnopqrstuvwxyz"
uppercase  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers    = "1234567890"
symbols    = "!@#$%^&*()_+-=[]/,.<>"


while 1:
    password_length   = int(input("How many characters would you like your password to have? "))
    lowercase_letters = int(input("How many lowercase letters would you like your password to have? "))
    uppercase_letters = int(input("How many uppercase letters would you like your password to have? "))
    symbols_count     = int(input("How many special characters would you like your password to have? "))
    password = ""
    if lowercase_letters + uppercase_letters + symbols_count == password_length:
        password = ""
        for x in range(0, lowercase_letters):
            password_set1 = random.choice(lowercase)
            password      = password + password_set1
        for x in range (0, uppercase_letters):
            password_set2 = random.choice(uppercase)
            password      = password + password_set2
        for x in range (0, symbols_count):
            password_set3 = random.choice(symbols)
            password = password + password_set3
        l = list(password)
        shuffle(l)
        password = ''.join(l)
        print ("Here is your password: ", password)
        break
    elif lowercase_letters + uppercase_letters + symbols_count != password_length:
        print()
        retry = input("The sum of your preferences should equal the password length. Would you like to try again (Y/N)? ")
        if retry == "y":
            continue
        elif retry == "Y":
            continue
        else:
            quit()
        
