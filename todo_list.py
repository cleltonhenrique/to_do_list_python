class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Tarefa "{task}" adicionada com sucesso!')

    def remove_task(self, task):
        if task in self.tasks:
            print(f"Tarefa '{task}'  encontrada!")
        else:
            print(f"Tarefa '{task}' não encontrada!")

    def show_tasks(self):
        if self.tasks:
            print("Lista de tarefas:")
            for index, task in enumerate(self.tasks):
                print(f"{index + 1} - {task}")
        else:
            print("A lista está vazia!")

