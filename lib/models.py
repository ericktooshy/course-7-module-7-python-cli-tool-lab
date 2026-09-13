class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False

    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")


class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []

    def add_task(self, title):
        task = Task(title) if isinstance(title, str) else title
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.username}.")
        return task