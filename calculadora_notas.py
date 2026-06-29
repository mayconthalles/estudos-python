def resultado(n1, n2):
    media = (n1 + n2) / 2
    print("Nota1: ", n1)
    print("Nota2: ", n2)
    print("Media: ", media)
    if media >= 7:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
resultado(n1, n2)
