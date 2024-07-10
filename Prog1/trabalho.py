def calcular_media(p1, p2, trabalho):
    return (4 * float(p1) + 4 * float(p2) + 2 * float(trabalho)) / 10

def print_arquivo(nome_arquivo, bool_media=False, bool_alf=False, bool_ord_media=False, bool_ind=False, bool_only_alunos=False):
    with open(nome_arquivo, 'r') as arquivo:
        alunos = []
        for linha in arquivo:
            dados = linha.strip().split('\t')
            nome, matricula, p1, p2, trabalho = dados
            
            if bool_media:
                media = calcular_media(p1, p2, trabalho)
                alunos.append((nome, matricula, p1, p2, trabalho, media))
            else:
                alunos.append((nome, matricula, p1, p2, trabalho))
                
        if bool_only_alunos:
            return alunos
        
        # Imprimindo cabeçalho
        if bool_ind:
            print(f"{'Ind':<4}{'Nome':<15}{'Matrícula':<13}{'P1':<5}{'P2':<5}{'Trabalho':<10}{'Média':<6}")
        elif bool_media:
            print(f"{'Nome':<15}{'Matrícula':<13}{'P1':<5}{'P2':<5}{'Trabalho':<10}{'Média':<6}")
        else:
            print(f"{'Nome':<15}{'Matrícula':<13}{'P1':<5}{'P2':<5}{'Trabalho':<10}")
                
        # Ordenações
        if bool_alf:
            alunos.sort(key=lambda aluno: aluno[0])
                
        if bool_ord_media:
            alunos.sort(key=lambda aluno: aluno[5], reverse=True)

        # Imprimindo dados dos alunos
        if bool_ind:
            for i, aluno in enumerate(alunos, 1):
                if bool_media:
                    nome, matricula, p1, p2, trabalho, media = aluno
                    print(f"{i:<4}{nome:<15}{matricula:<13}{p1:<5}{p2:<5}{trabalho:<10}{media:<6.2f}")
                else:
                    nome, matricula, p1, p2, trabalho = aluno
                    print(f"{i:<4}{nome:<15}{matricula:<13}{p1:<5}{p2:<5}{trabalho:<10}")
        else:
            for aluno in alunos:
                if bool_media:
                    nome, matricula, p1, p2, trabalho, media = aluno
                    print(f"{nome:<15}{matricula:<13}{p1:<5}{p2:<5}{trabalho:<10}{media:<6.2f}")
                else:
                    nome, matricula, p1, p2, trabalho = aluno
                    print(f"{nome:<15}{matricula:<13}{p1:<5}{p2:<5}{trabalho:<10}")

def op1():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo
    with open(nome_arquivo, 'a+') as arquivo:
        nome = input("Nome do aluno: ")
        matricula = input("Matrícula do aluno: ")
        p1 = input("Nota da P1: ")
        p2 = input("Nota da P2: ")
        trabalho = input("Nota do trabalho: ")

        linha = f"{nome}\t{matricula}\t{p1}\t{p2}\t{trabalho}\n"
        arquivo.write(linha)

        continuar = input("Deseja continuar? (S/N): ").strip().upper()
        if continuar == "S":
            op1()
        else:
            print("Dados gravados com sucesso.")
            main()

def op2():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo
    print_arquivo(nome_arquivo)

def op3():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo 
    print_arquivo(nome_arquivo, bool_media=True, bool_alf=True)

def op4():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo
    print_arquivo(nome_arquivo, bool_media=True, bool_ord_media=True)

def op5():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo
    nome_aluno = input("Qual o nome do aluno desejado? :")
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
            dados = linha.strip().split('\t')
            nome, matricula, p1, p2, trabalho = dados
            if nome_aluno == nome:
                media = calcular_media(p1, p2, trabalho)
                print("{:<15}{:<13}{:<5}{:<5}{:<10}{:<6}".format('Nome', 'Matrícula', 'P1', 'P2', 'Trabalho', 'Média'))
                print("{:<15}{:<13}{:<5}{:<5}{:<10}{:<6.2f}".format(nome, matricula, p1, p2, trabalho, media))
                return
        print("Aluno não encontrado.")

def op6():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo
    print_arquivo(nome_arquivo, bool_ind=True)
    alunos = print_arquivo(nome_arquivo, bool_only_alunos=True)
    indice = int(input("Qual aluno deseja editar (insira o índice): ")) - 1
    if 0 <= indice < len(alunos):
        nome, matricula, p1, p2, trabalho = alunos[indice]
        print("Deixe em branco se não quiser alterar um campo.")
        novo_nome = input(f"Nome ({nome}): ") or nome
        nova_matricula = input(f"Matrícula ({matricula}): ") or matricula
        nova_p1 = input(f"Nota da P1 ({p1}): ") or p1
        nova_p2 = input(f"Nota da P2 ({p2}): ") or p2
        novo_trabalho = input(f"Nota do trabalho ({trabalho}): ") or trabalho
        alunos[indice] = (novo_nome, nova_matricula, nova_p1, nova_p2, novo_trabalho)
    
    with open(nome_arquivo, 'w') as arquivo:
        for aluno in alunos:
            linha = "\t".join(aluno) + "\n"
            arquivo.write(linha)
    
    print("Dados do aluno atualizados com sucesso.")

def op7():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo
    with open(nome_arquivo, 'r') as arquivo:
        alunos = [linha.strip().split('\t') for linha in arquivo]
    
    nome_aluno = input("Nome do aluno a ser salvo: ")
    for aluno in alunos:
        if aluno[0] == nome_aluno:
            print("Dados do aluno já estão salvos.")
            return
    
    nome = input("Nome do aluno: ")
    matricula = input("Matrícula do aluno: ")
    p1 = input("Nota da P1: ")
    p2 = input("Nota da P2: ")
    trabalho = input("Nota do trabalho: ")

    linha = f"{nome}\t{matricula}\t{p1}\t{p2}\t{trabalho}\n"
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(linha)
    
    print("Dados do aluno salvos com sucesso.")

def op8():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo
    nome_aluno = input("Nome do aluno a ser apagado: ")
    
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    with open(nome_arquivo, 'w') as arquivo:
        for linha in linhas:
            if not linha.startswith(nome_aluno):
                arquivo.write(linha)
    
    print("Registro do aluno apagado com sucesso.")

def main():
    while True:
        print()
        print("Qual operação deseja realizar?")
        print("1 - Ler informações de um aluno a partir do teclado")
        print("2 - Ler informações dos alunos de um arquivo (especificando o nome do arquivo)")
        print("3 - Listar os alunos, com suas notas (incluindo uma média M=(4xP1+4xP2+2x trabalho)/10, em ordem alfabética)")
        print("4 - Listar os alunos, com suas notas (incluindo uma média M=(4xP1+4xP2+2x trabalho)/10, em ordem decrescente da média)")
        print("5 - Verificar se um aluno está no arquivo (e recuperar as informações dele)")
        print("6 - Editar as informações de um aluno.")
        print("7 - Salvar as informações de um aluno.")
        print("8 - Apagar no registro as informações de um aluno.")
        print("9 - Sair do programa")

        operacao = int(input("Escolha a operação (1-9): "))
        if operacao == 1:
            op1()
        elif operacao == 2:
            op2()
        elif operacao == 3:
            op3()
        elif operacao == 4:
            op4()
        elif operacao == 5:
            op5()
        elif operacao == 6:
            op6()
        elif operacao == 7:
            op7()
        elif operacao == 8:
            op8()
        elif operacao == 9:
            print("Programa encerrado")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

main()
