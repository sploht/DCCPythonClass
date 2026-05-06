# Code Your Import statments below to import your Contacts class as well as your search and sorting functions (you will build these yourself!!!!):
from algorithms import bubble_sort
from algorithms import binary_search
from phone_information import Contact

def print_list(contact_list):
    for index in range(len(contact_list)-1):
        print(contact_list[index])

def add_contact(contact_list):
    print("Enter the first name: ")
    new_contact_first = input()
    print('Enter the last name: ')
    new_contact_last = input()
    print("Enter the phone number: ")
    new_contact_ph = input()
    newContact = Contact(new_contact_first, new_contact_last, new_contact_ph)
    
    contact_list.append(newContact)
    bubble_sort(contact_list)


# ---------------------------------------- DO NOT MODIFY THE CODE BELOW THIS LINE ! IF YOU MODIFY THE BELOW CODE YOU WILL GET A 0 ! ---------------------------------------- #
# THIS CODE IS NECESSARY TO RUN YOUR FILES! 
#these imports let us create fake data below
#if the import does not work, open your Terminal and type: pip install Faker
from faker import Faker
# random lets the contact_list be extra shuffled so you can do your sorting algorithm
import random
#fake lets us create fake data
fake = Faker()

# Creates 11 instances of the Contact class (WHICH YOU MUST BUILD -- SEE PHONE_INFORMATION.PY), 10 of which use entirely random fake data
# NOTE: all of these calls (fake.first_name(), etc) return a string 
person1 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person2 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person3 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person4 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person5 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person6 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person7 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person8 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person9 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person10 = Contact(fake.first_name(), fake.last_name(), fake.phone_number())
person11 = Contact("Stephen", "Colbert", fake.phone_number())

# THIS IS THE CONTACT LIST YOU WILL BE USING BELOW to SEARCH THROUGH
contact_list = [person1, person2, person3, person4, person5, person6, person7, person8, person9, person10, person11]
# THE LIST HAS BEEN SHUFFLED. THIS WILL BE RANDOM EVERY TIME. YOU HAVE NO IDEA WHERE ANY CONTACT IS!
random.shuffle(contact_list)
# ---------------------------------------- DO NOT MODIFY THE CODE ABOVE THIS LINE ! IF YOU MODIFY THE ABOVE CODE YOU WILL GET A 0 ! ---------------------------------------- #

# Code the remainder of your program below. See assignment for requirements.

def main():
    bubble_sort(contact_list)
    choice = 0
    while choice != 4: 
        choice = 0
        print("**Menu**")
        print("Select one of the following options:")
        print("1: Show all contacts")
        print("2: Add a new contact")
        print("3: Search for a specific contact")
        print("4: Quit the program")
        print("Enter your selection: ")
        choice = int(input())

        if choice < 1 or choice > 4:
            print("\nThat is not a valid selection. Try again.\n")
        elif choice == 1:
            print_list(contact_list)
            print("\n")
        elif choice == 2:
            add_contact(contact_list)
            print("\n")
        elif choice == 3:
            print("What name do you want to find?")
            print("Enter first name: ")
            search_first_name = input()
            print("Enter last name: ")
            search_last_name = input()
            found_index = binary_search(contact_list, 0, len(contact_list)-1, person9)
            if found_index == -1:
                print("Contact not found")
            else:
                print(person9)
            print("\n")
        elif choice == 4:
            print("Goodbye")
            break
main()