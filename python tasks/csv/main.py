import csv
import os

CSVFILE = "csv/data.csv"


def initialize_csv():
    if not os.path.exists(CSVFILE) or os.path.getsize(CSVFILE) == 0:
        with open(CSVFILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["name", "age", "rate"])


def write_user():
    try:
        with open(CSVFILE, "a") as file:
            user_name = input("Enter Name: ")
            user_age = input("Enter Age: ")
            user_rate = input("Enter Rate: ")

            user = [user_name, user_age, user_rate]
            writer = csv.writer(file)
            writer.writerow(user)

            print("User added successfully!")
    except Exception as e:
        print(f"Error: {e}")


def read_users():
    with open(CSVFILE, "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        name = header.index("name")
        age = header.index("age")
        rate = header.index("rate")

        for row in reader:
            print(row[name], row[age], row[rate])


def user_to_list():
    with open(CSVFILE, "r") as file:
        reader = csv.reader(file)
        header = next(reader)

        name = header.index("name")
        age = header.index("age")
        rate = header.index("rate")

        users = []
        for row in reader:
            users.append({"name": row[name], "age": row[age], "rate": float(row[rate])})

        return users


def read_filtered_users(list):
    for user in list:
        print(
            "name: ", user["name"], " - age: ", user["age"], " - rate: ", user["rate"]
        )


def read_high_rated_users():
    list = user_to_list()
    new_list = []
    avg_rate = sum([user["rate"] for user in list]) / len(list)
    for user in list:
        if user["rate"] > avg_rate or user["rate"] == 5:
            new_list.append(user)
    read_filtered_users(new_list)


def read_average_user():
    list = user_to_list()
    new_list = []

    avg_age = sum([int(user["age"]) for user in list]) / len(list)

    oraliq = int(input("Enter oraliq (+-): "))

    for user in list:
        user_age = int(user["age"])
        if avg_age - oraliq <= user_age <= avg_age + oraliq:
            new_list.append(user)

    read_filtered_users(new_list)


def read_avarage_age():
    list = user_to_list()
    sum_age = sum([int(user["age"]) for user in list])
    print("Avarage age: ", sum_age / len(list))


def main():
    initialize_csv()
    while True:
        print("\n1. Add user")
        print("2. Read users")
        print("3. Read high rated users")
        print("4. Read avarage rated users")
        print("5. Avarage age")
        print("6. Exit\n")
        choice = input("Enter your choice: ")
        if choice == "1":
            write_user()
        elif choice == "2":
            read_users()
        elif choice == "3":
            read_high_rated_users()
        elif choice == "4":
            read_average_user()
        elif choice == "5":
            read_avarage_age()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    main()
