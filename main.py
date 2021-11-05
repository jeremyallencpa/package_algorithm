#Student Name: Jeremy W. Allen
#Student ID: 001305503

from menu import *

class Main:
    print(menu())
    user_input = input("Enter selection here: ")
    if user_input == '1':
        package_lookup()
    elif user_input == '2':
        package_list_with_status()
    elif user_input == '3':
        print_program_stats()
    elif user_input == '0':
        exit()
    else:
        print('Please entry a valid entry')