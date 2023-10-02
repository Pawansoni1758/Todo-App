FILEPATH = "lis.txt"


def lis_todo(filepath=FILEPATH):
    with open(filepath, "r") as file:
        lis = file.readlines()
    return lis


def write_lis(todo_arg, filepath=FILEPATH):
    with open(filepath, "w") as file:
        file.writelines(todo_arg)


if __name__=="__main__":
    print("this is using functions file")