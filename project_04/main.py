import json
from pathlib import Path

FILE_PATH = Path(__file__).parent / "contacts.json"
def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")

    person = {
        "name": name,
        "age": age,
        "email": email
    }

    return person

def display_people(people):
    for i, person in enumerate(people):
        print(i+1, "-", person["name"], "|", person["age"], "|", person["email"])

def load_people():
    with open(FILE_PATH, "r") as file:
        return json.load(file)["contacts"]

def save_people(people):
    with open(FILE_PATH, "w") as file:
        json.dump({"contacts": people}, file, indent=4)

def delete_contact(people):
    display_people(people)
    while True:
        number = input("Enter a number to delete")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range")
            else:
                people.pop(number-1)
                break
        except:
            print("Invalid number")

    print("Person deleted")

def search(people):
    search_name = input("Enter name to search for: ").lower()
    results = []
    for person in people:
        if search_name in person["name"].lower():
            results.append(person)
    if not results:
        print("\nPerson with that name doesn't exist in list.")
    else:
        print("-----------------")
        display_people(results)
        print("-----------------")

def main():
    print("Hi, welcome to the Contact Management System.")
    print()

    people = load_people()

    while True:
        print("\nContact list size:", len(people))
        command = input("\nYou can 'Add' person, 'Delete' person or 'Search' for a person ('q' for quit): ").lower()
        if command == "add":
            person = add_person()
            people.append(person)
        elif command == "delete":
            delete_contact(people)
        elif command == "search":
            search(people)
        elif command == "q":
            save_people(people)
            break
        else:
            print("\nInvalid command.\n")

    print(people)

if __name__ == "__main__":
    main()