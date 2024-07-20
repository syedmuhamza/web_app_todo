FILEPATH = "webtodos.txt"


def get_todos(filepath=FILEPATH):
    """ Reads the data from the filepath """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


# print(help(get_todos))


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the todo item in the text file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


print(__name__)
if __name__ == "__main__":
    print("Loading functions.py")
    print(get_todos())

