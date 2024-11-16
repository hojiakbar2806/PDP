import os

for i in os.listdir():
    print(f" - {i}")

cmd = input("\nEnter command: ")

if cmd == "create_file":
    file_name = input("File name: ")
    try:
        with open(file_name, "w") as new_file:
            new_file.write("")
        print("yaratildi")
    except FileNotFoundError as e:
        print(e, "topilmadi")

elif cmd == "copy_file":
    file_name = input("File name: ")
    data = open(file_name, "r").read()
    print("nusxa olindi")
    new_name = input("New file name: ")
    with open(new_name, "w") as new_file:
        new_file.write(data)
    print("yaratildi")

elif cmd == "create_folder":
    folder_name = input("File name: ")
    try:
        os.makedirs(folder_name, exist_ok=True)
        print("yaratildi")
    except FileExistsError:
        print(f" papkasi allaqachon mavjud.")

# os.rename("index.html", "about.html")

# os.remove("about.html")
