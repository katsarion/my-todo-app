FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):  # кастомная функция
    """ read a text file and return the list of
    to-do items.
    """
    with open(filepath, "r") as file_local:
        """write the to-dos items in the file"""
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_argument, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todos_argument)
        # return не надо, потому что эта кастомка исключительно для модификации текста(процедура)


print(__name__)
if __name__ == "__main__":  # проверка функций
    print("hello")
    print(get_todos())
