import tasks as tasks_
import config


def create(tasks):
    date = input("Date?")
    task = input("Task?")
    tasks.create(date, task)


def delete(tasks):
    date = input("Date?")
    index = int(input("Index?"))
    tasks.delete(date, index)


def update(tasks):
    date = input("Date?")
    index = int(input("Index?"))
    new_task = input("New task?")
    tasks.update(date, index, new_task)


def read(tasks):
    date = input("Date?")
    for index, task in enumerate(tasks.read(date)):
        print(f"{index}. {task}")


def default(_):
    print("Incorrect action")


actions = {
    "c": create,
    "r": read,
    "u": update,
    "d": delete,
    "q": lambda _: exit(),
}


def main():
    tasks = tasks_.Tasks(config.get_serializer())
    while True:
        print("""Task manager
        c - create
        r - read
        u - update
        d - delete
        q - quit""")
        action = input("Action?").lower()
        try:
            actions.get(action, default)(tasks)
        except (KeyError, IndexError):
            print("Incorrect data")


if __name__ == "__main__":
    main()
