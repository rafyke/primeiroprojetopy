notaA=float(input("Informe a primeira nota: "))
notaB=float(input("Informe a segunda nota: "))
    #calcular media
mediafinal = (notaA + notaB) / 2
#condição
if mediafinal >=7.0:
        print("Média: %.1f - Aprovado"% mediafinal)
else:
        print("Média: %.1f - Reprovado"% mediafinal)
