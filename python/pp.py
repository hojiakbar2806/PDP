def salom_hello(name: str):
    if isinstance(name, str):
        print( name)
    elif isinstance(name, int):
        raise ValueError("name type is not int")
    else:
        raise ValueError("Invalid value")


salom_hello("hojiakbar")
