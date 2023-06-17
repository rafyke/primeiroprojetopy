arquivo = open('arquivo.txt', 'w')
arquivo.write ('Curso Python n\n')
arquivo.write ('Aula Prática')
arquivo.close()
#testando a função leitura
leitura = open('arquivo.txt', 'r')
print(leitura.read())
leitura.close()