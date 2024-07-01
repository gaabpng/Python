# SEMPRE QUE ADICIONAR /PROG1 A UM ARQUIVO É SÓ POR CAUSA DA ORGANIZAÇÃO DE ARQUIVOS DO MEU PC

def calcular_media(p1, p2, trabalho):
    return (4 * float(p1) + 4 * float(p2) + 2 * float(trabalho)) / 10

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
            op5()
        else:
            arquivo.close()
            print("Dados gravados com sucesso.")
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
        print("{:<15}{:<13}{:<5}{:<5}{:<10}{:<6}".format('Nome', 'Matrícula', 'P1', 'P2', 'Trabalho', 'Média'))
        for aluno in alunos:
            nome, matricula, p1, p2, trabalho, media = aluno
            print("{:<15}{:<13}{:<5}{:<5}{:<10}{:<6.2f}".format(nome, matricula, p1, p2, trabalho, media))

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


        print(f"{'Nome':<15}{'Matrícula':<13}{'P1':<5}{'P2':<5}{'Trabalho':<10}{'Média':<6}")
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
    nome_aluno = input("Qual o nome do aluno desejado? :")
    with open(nome_arquivo, 'r') as arquivo:
        alunos = []
        for linha in arquivo:
            dados = linha.strip().split('\t')
            nome, matricula, p1, p2, trabalho = dados
            media = calcular_media(p1, p2, trabalho)
            alunos.append((nome, matricula, p1, p2, trabalho, media))
        print("{:<15}{:<13}{:<5}{:<5}{:<10}{:<6}".format('Nome', 'Matrícula', 'P1', 'P2', 'Trabalho', 'Média'))
        for aluno in alunos:
            if nome_aluno == nome:
                nome, matricula, p1, p2, trabalho, media = aluno
                print("{:<15}{:<13}{:<5}{:<5}{:<10}{:<6.2f}".format(nome, matricula, p1, p2, trabalho, media))

def op6():
    nome_arquivo = input("Nome do arquivo: ")
    nome_arquivo = "Prog1/" + nome_arquivo
    with open(nome_arquivo, 'r') as arquivo:
        alunos = []
        i = 0
        for linha in arquivo:
            dados = linha.strip().split('\t')
            nome, matricula, p1, p2, trabalho = dados
            media = calcular_media(p1, p2, trabalho)
            alunos.append((nome, matricula, p1, p2, trabalho, media))
        print(linha + "{:<4}{:<15}{:<13}{:<5}{:<5}{:<10}{:<6}".format('Ind', 'Nome', 'Matrícula', 'P1', 'P2', 'Trabalho', 'Média'))
        for aluno in alunos:
            i = i+1
            nome, matricula, p1, p2, trabalho, media = aluno
            print("{:<4}{:<15}{:<13}{:<5}{:<5}{:<10}{:<6.2f}".format(i, nome, matricula, p1, p2, trabalho, media))
            arquivo.close()
    edit = input("Qual aluno deseja editar (insira o indice)")


    rep = input("Deseja editar mais algum aluno?: (S/N)")
    if rep == "S":
        op6()

def op7():
    print("feat8")

def op8():
    print("feat8")
def main():
    while True:
        print("Qual operação deseja realizar?")
        print("1 - Ler informações de um aluno a partir do teclado")
        print("2 - Ler informações dos alunos de um arquivo (especificando o nome do arquivo)")
        print("3 - Listar os alunos, com suas notas (incluindo uma média M=(4xP1+4xP2+2x trabalho)/10, em ordem alfabética)")
        print("4 - Listar os alunos, com suas notas (incluindo uma média M=(4xP1+4xP2+2x trabalho)/10, em ordem decrescente da média)")
        print("5 - Gravar as informações dos alunos em um arquivo (especificando o nome do arquivo)")
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
