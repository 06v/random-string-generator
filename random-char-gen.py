# Date: 12/19/2020
# Author: Enes
# Description: Random Character / String Generator

import os
import csv
import sys
import string
import random
from colorama import Fore, init

os.system("cls")

init()

def main():
   menu()


def menu():
    print(f"""{Fore.CYAN}
╔═╗┬ ┬┌─┐┬─┐  ╔═╗┌─┐┌┐┌
║  ├─┤├─┤├┬┘  ║ ╦├┤ │││
╚═╝┴ ┴┴ ┴┴└─  ╚═╝└─┘┘└┘{Fore.RESET}""")

    choice = input(f"""
{Fore.LIGHTYELLOW_EX}[1]{Fore.RESET} Custom Letters
{Fore.LIGHTYELLOW_EX}[2]{Fore.RESET} Strong Password/s
{Fore.LIGHTYELLOW_EX}[3]{Fore.RESET} Letters and Numbers
{Fore.LIGHTYELLOW_EX}[4]{Fore.RESET} Without repeating Characters
{Fore.LIGHTYELLOW_EX}[5]{Fore.RESET} Lower-Case and Upper-Case Letters
{Fore.LIGHTYELLOW_EX}[6]{Fore.RESET} Exit

What do you want to do? \n» """)
    print()

    if choice == "1":
        custom()
    elif choice == "2":
        strongpw()
    elif choice == "3":
        letnum()
    elif choice == "4":
        norep()
    elif choice == "5":
        uplow()
    elif choice == "6":
        sys.exit
    else:
        print("Select a valid option.. \n Please repeat.")
        menu()

def custom():
    sample_letters = input('Which Letters / Numbers should the Characters contain? \n» ')
    print()
    length = int(input("How many Characters in one? \n» "))
    print()
    number = int(input("How many do you want to generate? \n» "))
    print()
    for i in range(number):
        result_str = ''.join((random.choice(sample_letters) for i in range(length)))
        print(result_str)
        with open('custom.txt', "a") as x:
            x.write(f"{result_str}\n")
    yesno = input("\nDo you want to save them into an Text File? \n» ")
    if str(yesno).startswith("n" or "N"):
        os.remove("custom.txt")
        print("\nDone without Saving! Press Enter to Exit.")
        input()
    else:
        print("\nDone! Press Enter to Exit.")
        input()

def strongpw():
    password_characters = string.ascii_letters + string.digits + string.punctuation
    length = int(input("How many Characters in one? \n» "))
    print()
    number = int(input("How many do you want to generate? \n» "))
    print()
    for i in range(number):
        password = ''.join(random.choice(password_characters) for i in range(length))
        print(password)
        with open('passwords.txt', "a") as x:
            x.write(f"{password}\n")
    yesno = input("\nDo you want to save them into an Text File? \n» ")
    if str(yesno).startswith("n" or "N"):
        os.remove("passwords.txt")
        print("\nDone without Saving! Press Enter to Exit.")
        input()
    else:
        print("\nDone! Press Enter to Exit.")
        input()

def letnum():
    letters_and_digits = string.ascii_letters + string.digits
    length = int(input("How many Characters in one? \n» "))
    print()
    number = int(input("How many do you want to generate? \n» "))
    print()
    for i in range(number):
        result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
        print(result_str)
        with open('lettersnumbers.txt', "a") as x:
            x.write(f"{result_str}\n")
    yesno = input("\nDo you want to save them into an Text File? \n» ")
    if str(yesno).startswith("n" or "N"):
        os.remove("lettersnumbers.txt")
        print("\nDone without Saving! Press Enter to Exit.")
        input()
    else:
        print("\nDone! Press Enter to Exit.")
        input()


def norep():
    letters = string.ascii_lowercase
    length = int(input("How many Characters in one? \n» "))
    print()
    number = int(input("How many do you want to generate? \n» "))
    print()
    for i in range(number):
        result_str = ''.join(random.sample(letters, length))
        print(result_str)
        with open('norepeat.txt', "a") as x:
            x.write(f"{result_str}\n")
    yesno = input("\nDo you want to save them into an Text File? \n» ")
    if str(yesno).startswith("n" or "N"):
        os.remove("norepeat.txt")
        print("\nDone without Saving! Press Enter to Exit.")
        input()
    else:
        print("\nDone! Press Enter to Exit.")
        input()
    
def uplow():
    length = int(input("How many Characters in one? \n» "))
    print()
    number = int(input("How many do you want to generate? \n» "))
    letters = string.ascii_letters
    for i in range(number):
        result_str = ''.join(random.choice(letters) for i in range(length))
        print(result_str)
        with open('chars.txt', "a") as x:
            x.write(f"{result_str}\n")
    yesno = input("\nDo you want to save them into an Text File? \n» ")
    if str(yesno).startswith("n" or "N"):
        os.remove("chars.txt")
        print("\nDone without Saving! Press Enter to Exit.")
        input()
    else:
        print("\nDone! Press Enter to Exit.")
        input()

main()