'''
def get_todos(filepath="todos.txt"): #Function to read todos
    with open(filepath, 'r') as file:
        to_list_local = file.readlines()
    return to_list_local

def write_todos(to_list_arg, filepath = "todos.txt"):
    with open(filepath, 'w') as file:
        file.writelines(to_list_arg)
'''
file_name = "todos.txt"

def get_todos(filepath=file_name): #Function to read todos
    with open(filepath, 'r') as file:
        to_list_local = file.readlines()
    return to_list_local

def write_todos(to_list_arg, filepath = file_name):
    with open(filepath, 'w') as file:
        file.writelines(to_list_arg)
