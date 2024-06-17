# SEMPRE QUE ADICIONAR /PROG1 A UM ARQUIVO É SÓ POR CAUSA DA ORGANIZAÇÃO DE ARQUIVOS DO MEU PC

def calcular_media(p1, p2, trabalho):
    return (4 * float(p1) + 4 * float(p2) + 2 * float(trabalho)) / 10

def op1():
    nome = input("Nome do aluno: ")
    matricula = input("Matrícula do aluno: ")
    p1 = input("Nota da P1: ")
    p2 = input("Nota da P2: ")
    trabalho = input("Nota do trabalho: ")

    print("Nome: ", nome)
    print("Matrícula: ", matricula)
    print("Nota da P1: ", p1)
    print("Nota da P2: ", p2)
    print("Nota do trabalho: ", trabalho)

    continuar = input("Deseja continuar? (S/N): ")
    if continuar == "S":
        op1()
    else:
        print("Programa encerrado")
        main()

def op2():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo

    with open(nome_arquivo, 'r') as arquivo:
        alunos = []
        for linha in arquivo:
            dados = linha.strip().split('\t')
            nome, matricula, p1, p2, trabalho = dados
            media = calcular_media(p1, p2, trabalho)
            alunos.append((nome, matricula, p1, p2, trabalho, media))
        print("{:<15}{:<10}{:<5}{:<5}{:<10}{:<6}".format('Nome', 'Matrícula', 'P1', 'P2', 'Trabalho', 'Média'))
        for aluno in alunos:
            nome, matricula, p1, p2, trabalho, media = aluno
            print("{:<15}{:<10}{:<5}{:<5}{:<10}{:<6.2f}".format(nome, matricula, p1, p2, trabalho, media))

def op3():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo 


    with open(nome_arquivo, 'r') as arquivo:
        alunos = []
        for linha in arquivo:
            dados = linha.strip().split('\t')
            nome, matricula, p1, p2, trabalho = dados
            media = calcular_media(p1, p2, trabalho)
            alunos.append((nome, matricula, p1, p2, trabalho, media))


        alunos.sort(key=lambda aluno: aluno[0])


        print(f"{'Nome':<15}{'Matrícula':<10}{'P1':<5}{'P2':<5}{'Trabalho':<10}{'Média':<6}")
        for aluno in alunos:
            nome, matricula, p1, p2, trabalho, media = aluno
            print(f"{nome:<15}{matricula:<10}{p1:<5}{p2:<5}{trabalho:<10}{media:<6.2f}")

def op4():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo


    with open(nome_arquivo, 'r') as arquivo:
        alunos = []
        for linha in arquivo:
            dados = linha.strip().split('\t')
            if len(dados) == 5:  # Assegurando que há exatamente 5 colunas
                nome, matricula, p1, p2, trabalho = dados
                media = calcular_media(p1, p2, trabalho)
                alunos.append((nome, matricula, p1, p2, trabalho, media))

        alunos.sort(key=lambda aluno: aluno[5], reverse=True)

        print("{:<15}{:<10}{:<5}{:<5}{:<10}{:<6}".format('Nome', 'Matrícula', 'P1', 'P2', 'Trabalho', 'Média'))
        for aluno in alunos:
            nome, matricula, p1, p2, trabalho, media = aluno
            print("{:<15}{:<10}{:<5}{:<5}{:<10}{:<6.2f}".format(nome, matricula, p1, p2, trabalho, media))

def op5():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo
    with open(nome_arquivo, 'a+') as arquivo:
        nome = input("Nome do aluno: (SEM ESPAÇO) ")
        matricula = input("Matrícula do aluno: ")
        p1 = input("Nota da P1: ")
        p2 = input("Nota da P2: ")
        trabalho = input("Nota do trabalho: ")

        linha = f"{nome}\t{matricula}\t{p1}\t{p2}\t{trabalho}\n"
        arquivo.write(linha)

        continuar = input("Deseja continuar? (S/N): ").strip().upper()
        if continuar == "S":
            op5()
        else:
            arquivo.close()
            print("Dados gravados com sucesso.")
            main()

def main():
    while True:
        print("Qual operação deseja realizar?")
        print("1 - Ler informações de um aluno a partir do teclado")
        print("2 - Ler informações dos alunos de um arquivo (especificando o nome do arquivo)")
        print("3 - Listar os alunos, com suas notas (incluindo uma média M=(4xP1+4xP2+2x trabalho)/10, em ordem alfabética)")
        print("4 - Listar os alunos, com suas notas (incluindo uma média M=(4xP1+4xP2+2x trabalho)/10, em ordem decrescente da média)")
        print("5 - Gravar as informações dos alunos em um arquivo (especificando o nome do arquivo)")
        print("6 - Sair do programa")

        operacao = int(input("Escolha a operação (1-6): "))
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
            print("Programa encerrado")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

main()