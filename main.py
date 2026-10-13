# ============================================================
# Hard Project: Gym Membership Management System
# ============================================================

import os
import time

class Member:
    def __init__(self, first_name, last_name, membership_id, membership_status):
        self.first_name = first_name
        self.last_name = last_name
        self.membership_id = membership_id
        self.membership_status = membership_status

    def display_info(self):
        print(f"ID: {self.membership_id} | Name: {self.first_name} {self.last_name} | Status: {self.membership_status}")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_member():
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    membership_id = input("Enter Membership ID: ")
    membership_status = input("Enter Status (Active/Inactive): ")
    return Member(first_name, last_name, membership_id, membership_status)

def search_member(members):
    search_id = input("Enter Membership ID to search: ")
    found = False
    for member in members:
        if member.membership_id == search_id:
            print("\n✅ Member Found:")
            member.display_info()
            found = True
            break
    if not found:
        print("\n❌ Member not found!")

members = []

while True:
    clear_screen()
    print("====================================")
    print(" Welcome to Gym Membership Management")
    print("====================================")
    print("Choose an action:")
    print("1. Add new member")
    print("2. Display all members")
    print("3. Search for a member")
    print("4. Exit\n")

    choice = input("Enter your choice: ")

    if choice == '1':
        members.append(create_member())
        print("\nMember added successfully!")
        time.sleep(1.5)
    elif choice == '2':
        clear_screen()
        print("--- Gym Members List ---")
        if not members:
            print("No members registered yet.")
        else:
            for member in members:
                member.display_info()
        input("\nPress Enter to return to menu...")
    elif choice == '3':
        clear_screen()
        search_member(members)
        input("\nPress Enter to return to menu...")
    elif choice == '4':
        print("\nExiting Gym Management System. Goodbye!")
        break
    else:
        print("\nInvalid option!")
        time.sleep(1)
