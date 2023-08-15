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

def main():
    todo_list = ToDoList()

    while True:
        print("1 - Adicionar tarefa")
        print("2 - Remover tarefa")
        print("3 - Mostrar tarefas")
        print("4 - Sair")
        option = int(input("Escolha uma opção: "))

        if option == 1:
            task = input("Digite a tarefa: ")
            todo_list.add_task(task)
        elif option == 2:
            task = input("Digite a tarefa: ")
            todo_list.remove_task(task)
        elif option == 3:
            todo_list.show_tasks()
        elif option == 4:
            break
        else:
            print("Opção inválida!")

if __name__ == '__main__':
    main()
