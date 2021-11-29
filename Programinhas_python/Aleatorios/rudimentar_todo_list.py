import os


todolist = []
def todo_list():
    os.system("cls")
    for item in todolist:
        print(item)
    item = input(": ")
    todolist.append(item)

if __name__ == "__main__":
    while True:
        todo_list()

           
