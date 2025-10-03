# boas vindas

print("---Seja bem vindo---")

#lista vazia

tarefas = []

while True:

    #lista de opções menu

    print("\n--- Lista de Tarefas ---")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    #variavel opção

    opcao=int(input("Insira a opção desejada:  "))

    # pedir nome da tarefa
    # adicionar na lista com append
    # mostrar mensagem confirmando

    if opcao ==1:
        tarefas.append(input("Insira a tarefa: "))
        print("Tarefa Cadastrada com sucesso")

    elif opcao ==2:
        if len(tarefas) == 0:
            print("não há Registros")
        else:
            for i, t in enumerate(tarefas, start=1):
                print(i, "-", t)
        
    elif opcao ==3:
        if len(tarefas) == 0:
            print("não há Registros")
        else:
            for i, t in enumerate(tarefas, start=1):
                print(i, "-", t)
            try:
                numero =int(input("indique o n° da tarefa que deseja remover: "))
                tarefas.pop(numero -1)
                print("tarefa removida com sucesso!")
            except (ValueError, IndexError):
                print("Numero Inválido!")

         #Sair do programa

    if opcao == 4:
        print("Até Mais")
        break
