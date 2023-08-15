from todo_list import ToDoList

class MainApp:

    def __init__(self):
        self.todo_list = ToDoList()

    def run(self):
        while True:
            print("1 - Adicionar tarefa")
            print("2 - Remover tarefa")
            print("3 - Mostrar tarefas")
            print("4 - Sair")
            option = int(input("Escolha uma opção: "))

            if option == 1:
                task = input("Digite a tarefa: ")
                self.todo_list.add_task(task)
            elif option == 2:
                task = input("Digite a tarefa: ")
                self.todo_list.remove_task(task)
            elif option == 3:
                self.todo_list.show_tasks()
            elif option == 4:
                break
            else:
                print("Opção inválida!")

if __name__ == '__main__':
    main_app = MainApp()
    main_app.run()
