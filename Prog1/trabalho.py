def calcular_media(p1, p2, trabalho):
    return (4 * float(p1) + 4 * float(p2) + 2 * float(trabalho)) / 10

def print_arquivo(nome_arquivo, bool_media, bool_alf, bool_ord_media, bool_ind, bool_only_alunos):
    with open(nome_arquivo, 'r') as arquivo:
        alunos = []
        for linha in arquivo:
            dados = linha.strip().split('\t')
            nome, matricula, p1, p2, trabalho = dados
            
            if bool_media == True:
                media = calcular_media(p1, p2, trabalho)
                alunos.append((nome, matricula, p1, p2, trabalho, media))
            else:
                alunos.append((nome, matricula, p1, p2, trabalho))
                
        if bool_only_alunos == True:
            return alunos
        
        if bool_ind == True:
            print(f"{'Ind':<4}{'Nome':<15}{'Matrícula':<13}{'P1':<5}{'P2':<5}{'Trabalho':<10}{'Média':<6}")
        elif bool_media == True:
            print(f"{'Nome':<15}{'Matrícula':<13}{'P1':<5}{'P2':<5}{'Trabalho':<10}{'Média':<6}")
        else:
            print(f"{'Nome':<15}{'Matrícula':<13}{'P1':<5}{'P2':<5}{'Trabalho':<10}")
                
        if bool_alf == True:
            alunos.sort(key=lambda aluno: aluno[0])
                
        if bool_ord_media == True:
            alunos.sort(key=lambda aluno:aluno[5], reverse=True)

        if bool_media == True:                
            for aluno in alunos:
                nome, matricula, p1, p2, trabalho, media = aluno
                print(f"{nome:<15}{matricula:<13}{p1:<5}{p2:<5}{trabalho:<10}{media:<6.2f}")
        elif bool_ind == True:
            for i, aluno in enumerate(alunos, 1):
                nome, matricula, p1, p2, trabalho = aluno
                print("{:<4}{:<15}{:<13}{:<5}{:<5}{:<10}".format(i, nome, matricula, p1, p2, trabalho))             
                   
        else:
            for aluno in alunos:
                nome, matricula, p1, p2, trabalho = aluno
                print(f"{nome:<15}{matricula:<13}{p1:<5}{p2:<5}{trabalho:<10}")
        return alunos
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
            arquivo.close()
            print("Dados gravados com sucesso.")
            main()

def op2():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo
    print_arquivo(nome_arquivo, False, False, False, False, False)
    
def op3():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo 
    print_arquivo(nome_arquivo, True, True, False, False, False)
    
    
def op4():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo
    print_arquivo(nome_arquivo, True, False, True, False, False)
    
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
        arquivo.close()

def op6():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo
    print_arquivo(nome_arquivo, False, True, False, True, False)
    alunos = print_arquivo(nome_arquivo, False, False, False, False, True)
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
    arquivo.close()
def op7():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo
    with open(nome_arquivo, 'r') as arquivo:
        alunos = []
        for linha in arquivo:
            dados = linha.strip().split('\t')
            alunos.append(dados)
    
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
    arquivo.close()

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
    arquivo.close()
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