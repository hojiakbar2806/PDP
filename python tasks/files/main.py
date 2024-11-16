import os
import shutil


comands = {
    "for_file": [
        {
            "cmd": "create_file",
            "description": "Yangi file qo'shish",
        },
        {
            "cmd": "delete_file",
            "description": "File o'chirish",
        },
        {
            "cmd": "copy_file",
            "description": "File kopiyalash",
        },
        {
            "cmd": "rename_file",
            "description": "File nomini yangilash",
        },
        {
            "cmd": "file_info",
            "description": "File haqida ma'lumot",
        },
        {
            "cmd": "show_files",
            "description": "Barcha fileni ko'rish",
        },
    ],
    "for_folder": [
        {
            "cmd": "create_folder",
            "description": "Yangi folder qo'shish",
        },
        {
            "cmd": "delete_folder",
            "description": "Folder o'chirish",
        },
        {
            "cmd": "show_folders",
            "description": "Barcha folderni ko'rish",
        },
        {
            "cmd": "rename_folder",
            "description": "Folder yangilash",
        },
    ],
    "for_system": [
        {
            "cmd": "help",
            "description": "Yordam",
        },
        {
            "cmd": "clear",
            "description": "O'chirish",
        },
        {
            "cmd": "show_all",
            "description": "Barchasini ko'rish",
        },
        {
            "cmd": "exit",
            "description": "Chiqish",
        },
    ],
}


def show_all(dir=os.getcwd(), file_type="all"):
    print("\n" + dir)
    try:
        f_list = os.listdir(dir)
        if file_type == "all":
            print("Barcha fayl va papkalar:\n")
            for f in f_list:
                print(f"- {f}")
        if file_type == "files":
            print("\nFayllar:\n")
            for f in f_list:
                if os.path.isfile(os.path.join(dir, f)):
                    print(f"- {f}")
        if file_type == "folders":
            print("\nPapkalar:\n")
            for f in f_list:
                if os.path.isdir(os.path.join(dir, f)):
                    print(f"- {f}")
        print("\n")

    except FileNotFoundError:
        print(f"Katalog topilmadi: {dir}")


def is_exist_cmd(cmd_in):
    for cmd in comands["for_file"]:
        if cmd["cmd"] == cmd_in:
            return True

    for cmd in comands["for_folder"]:
        if cmd["cmd"] == cmd_in:
            return True

    for cmd in comands["for_system"]:
        if cmd["cmd"] == cmd_in:
            return True

    return False


def create_file():
    file_path = input("Which directory and file: ")
    dir_path, file_name = os.path.split(file_path)

    if dir_path == "":
        dir_path = os.getcwd()

    if not os.path.exists(dir_path):
        print(f"Directory '{dir_path}' not found.")
        return

    with open(os.path.join(dir_path, file_name), "w") as f:
        f.write("")
        print(f"Created file: {file_path}")


def delete_file():
    dir = os.getcwd()
    show_all(dir, file_type="files")

    file_path = input("File name to delete: ")

    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"File '{file_path}' successfully deleted.")
    else:
        print(f"File '{file_path}' not found.")


def rename_file():
    file_path = input("Which file: ")
    file_dir, file_name = os.path.split(file_path)
    if os.path.exists(os.path.join(file_dir, file_name)):
        new_name = input("New name: ")
        try:
            os.rename(file_path, os.path.join(file_dir, new_name))
        except FileExistsError:
            print(f"File '{new_name}' already exists.")
            return
        print(f"File '{file_path}' successfully renamed to '{new_name}'.")
    else:
        print(f"File '{file_path}' not found.")


def copy_write():
    file_path = input("Which file: ")
    if not os.path.exists(file_path):
        print(f"File '{file_path}' not found.")
        return
    new_path = input("Where to copy: ")
    if new_path == "":
        new_path = os.getcwd()
    if not os.path.exists(new_path):
        print(f"Directory '{new_path}' not found.")
        return

    try:
        shutil.copy(file_path, new_path)
        print(f"File '{file_path}' successfully copied to '{new_path}'.")
    except shutil.SameFileError:
        print(f"File '{file_path}' and '{new_path}' are the same directory")


def file_info():
    file_path = input("Which file: ")
    if os.path.exists(file_path):
        file_stats = os.stat(file_path)
        print(f"\nFile Name: {os.path.basename(file_path)}")
        print(f"File Size: {file_stats.st_size} bytes")
        print(f"Last Modified: {os.path.getmtime(file_path)}")
        print(f"Last Accessed: {os.path.getatime(file_path)}")
        print(f"Created: {os.path.getctime(file_path)}")
        print(f"File Mode: {oct(file_stats.st_mode)}")
        print(f"Is a directory: {os.path.isdir(file_path)}")
    else:
        print(f"File '{file_path}' not found.")


def show_cmd(for_what):
    if for_what == "for_file":
        print("\nFile commands:")
    elif for_what == "for_folder":
        print("\nFolder commands:")
    elif for_what == "for_system":
        print("\nSystem commands:")
    for cmd in comands[for_what]:
        print(f"""   {cmd['cmd']}  -  {cmd['description']}""")


def create_folder():
    folder_path = input("Folder name: ")
    dir, folder_name = os.path.split(folder_path)

    if dir == "":
        dir = os.getcwd()

    folder_dir = os.path.join(dir, folder_name)
    if not os.path.exists(dir):
        print(f"Directory '{dir}' not found.")
        return

    if os.path.exists(folder_dir):
        print(f"Directory '{folder_dir}' already exists.")
        return
    os.mkdir(folder_dir)
    print(f"Created folder: {folder_name}")


def delete_folder():
    show_all(dir, "folders")
    folder_name = input("Which folder: ")
    path = os.path.join(dir, folder_name)
    if os.path.exists(path):
        try:
            if not os.listdir(path):
                os.rmdir(path)
                print(f"Directory '{path}' successfully deleted.")
            else:
                confirm = input(
                    f"Directory '{path}' is not empty. Delete anyway? (y/n): "
                )
                if confirm.lower() == "y":
                    shutil.rmtree(path)
                    print(f"Directory '{path}' and all its contents deleted.")
                else:
                    print("Directory not deleted.")
        except OSError as e:
            print(f"Error: {e}")
    else:
        print(f"Directory '{path}' not found.")


def rename_folder():
    folder_path = input("Which folder: ")
    if os.path.exists(folder_path):
        new_name = input("New name: ")
        os.rename(folder_path, new_name)
        print(f"Directory '{folder_path}' successfully renamed to '{new_name}'.")
    else:
        print(f"Directory '{folder_path}' not found.")


while True:
    cmd = input("\nhelp - show commands\nCommand: ")

    if is_exist_cmd(cmd):
        match cmd:
            case "help":
                show_cmd("for_file")
                show_cmd("for_folder")
                show_cmd("for_system")

            case "create_file":
                create_file()

            case "delete_file":
                delete_file()

            case "show_files":
                dir = input("Directory: ")
                show_all(dir)

            case "copy_file":
                copy_write()
                
            case "copy_file":
                create_file()

            case "file_info":
                file_info()

            case "rename_file":
                rename_file()

            case "show_folders":
                dir = input("Which directory: ")
                show_all(dir, "folders")

            case "create_folder":
                create_folder()

            case "delete_folder":
                delete_folder()

            case "rename_folder":
                rename_folder()
                
            case "exit":
                break
            case "clear":
                os.system("clear")
            case _:
                pass
    else:
        print("Command not found commands.")
