class Tasks:
    def __init__(self, serializer):
        self.serializer = serializer
        self.tasks = self.serializer.load()

    def read(self, date):
        return self.tasks[date]

    def create(self, date, task):
        if date not in self.tasks:
            self.tasks[date] = [task]
        else:
            self.tasks[date].append(task)
        self.serializer.save(self.tasks)

    def delete(self, date, index):
        self.tasks[date].pop(index)
        self.serializer.save(self.tasks)

    def update(self, date, index, new_task):
        self.tasks[date][index] = new_task
        self.serializer.save(self.tasks)
