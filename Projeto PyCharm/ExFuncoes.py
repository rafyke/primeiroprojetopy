def lernotas():
    n = float(input('Digite uma nota para o aluno: '))
    return n


def resultado(n1, n2):
    media = (n1 + n2) / 2
    print(" A primeira nota: ", n1)
    print(" A segunda nota: ", n2)
    print("Média: ", media, "\nResultado: ", end=" ")
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


a = lernotas()
b = lernotas()
resultado(a, b)