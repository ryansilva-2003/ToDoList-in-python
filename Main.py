tarefas = []

def addTaref():
    tarefa = input("Por favor adicione uma tarefa: ")
    tarefas.append(tarefa)
    print(f"tarefa '{tarefa}' adicionada com sucesso")

def listTaref():
    if not tarefas:
        print("Sem registros de tarefas")
    else:
        print("Tarefas atuais:")
        for index, tarefa in enumerate(tarefas, start=1):
            print(f"Tarefa #{index}. {tarefa}")

def deleteTaref():
    listTaref()
    try:
        tarefaToDelete = int(input("Digite o numero da tarefa que deseja remover: "))
        if tarefaToDelete >= 0 and tarefaToDelete <= len(tarefas):
            tarefas.pop(tarefaToDelete - 1)
            print(f"A tarefa {tarefaToDelete} foi removida com sucesso.")
        else:
            print(f"A tarefa #{tarefaToDelete}  não foi encontrada.")
    except:
        print("Numero invalido")

if __name__ == "__main__":
    print("Bem-vindo a LISTA DE TAREFAS EM PYTHON")
    while True:
        print("------------------------------------")
        print("Por favor selecione a opção desejada")
        print("------------------------------------")
        print("1. Adicionar tarefa")
        print("2. Listar tarefa")
        print("3. Deletar tarefa")
        print("4. Sair")

        escolha = input("Escolha a opção: ")

        if escolha == "1":
            addTaref()
        elif escolha == "2":
            listTaref()
        elif escolha == "3":
            deleteTaref()
        elif escolha == "4":
            print("----------------------------------------------")
            print("Obrigado por usar a LISTA DE TAREFAS EM PYTHON")
            break
        else:
            print("Numero invalido. Por favor tente novamente.")
