tarefas = []

def adicionar_tarefa():
    nome = input("Nome da tarefa: ")
    descricao = input("Descrição: ")
    prioridade = input("Prioridade (Alta, Média, Baixa): ").capitalize()
    categoria = input("Categoria: ")

    tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade,
        "categoria": categoria,
        "concluida": False
    }

    tarefas.append(tarefa)
    print("✅ Tarefa adicionada com sucesso!")

def listar_tarefas(filtrar=None, valor=None):
    print("\n📋 Lista de Tarefas:")
    for i, t in enumerate(tarefas):
        if filtrar and t[filtrar] != valor:
            continue
        status = "✔" if t["concluida"] else "✘"
        print(f"{i}. [{status}] {t['nome']} - {t['prioridade']} - {t['categoria']}")

def marcar_concluida():
    listar_tarefas()
    try:
        i = int(input("Digite o número da tarefa a marcar como concluída: "))
        tarefas[i]["concluida"] = True
        print("✅ Tarefa marcada como concluída.")
    except (IndexError, ValueError):
        print("❌ Número inválido.")

def exibir_por_prioridade():
    prioridade = input("Digite a prioridade (Alta, Média, Baixa): ").capitalize()
    listar_tarefas(filtrar="prioridade", valor=prioridade)

def exibir_por_categoria():
    categorias = {t["categoria"] for t in tarefas}
    print("Categorias disponíveis:", ", ".join(categorias))
    categoria = input("Digite a categoria: ")
    listar_tarefas(filtrar="categoria", valor=categoria)

def menu():
    while True:
        print("\n=== Menu ===")
        print("1. Adicionar tarefa")
        print("2. Listar todas as tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Exibir por prioridade")
        print("5. Exibir por categoria")
        print("6. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa()
        elif escolha == "2":
            listar_tarefas()
        elif escolha == "3":
            marcar_concluida()
        elif escolha == "4":
            exibir_por_prioridade()
        elif escolha == "5":
            exibir_por_categoria()
        elif escolha == "6":
            print("Encerrando programa.")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
