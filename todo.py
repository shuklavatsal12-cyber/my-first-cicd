# create a simple todo list

todos = []

def add_task(task):
    # add task to todos list
    # write code here
    todos.append(task)


def remove_task(task):
    # remove task from todos list
    # write code here
    todos.remove(task)


def show_tasks():
    # print all tasks
    # write code hereor i, task in enumerate(todos, start=1):
        print(f"{i}. {task}")


# test it
add_task("Buy groceries")
add_task("Study AWS")
add_task("Exercise")
show_tasks()
# should print:
# 1. Buy groceries
# 2. Study AWS
# 3. Exercise

remove_task("Buy groceries")

show_tasks()
# should print:
# 1. Study AWS
# 2. Exercise


