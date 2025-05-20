# Crie uma lista apenas com elementos numéricos
lista = [1, 2377.90, 1,78, 1989-4-19, 365, 7.90]
print(lista)

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
lista = [1, 2.5, '1989-4-19', 'Giulia', 'Av:Braz Olaia, 230', 'True', 'CREDITO', '1,72*73kg']

# Imprima na tela apenas os 5 primeiros elementos da lista
print(lista[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
elementos_indice_par = lista[::2]
print(elementos_indice_par)

# Remova da lista o último item
lista.remove('1,72*73kg')

# Insira na lista um novo item
lista.append('electro')
print(lista)

# Remova da lista um item específico
lista.remove(1)
print(lista)

#lista = []
#numerica = [1, 2, 3, 4, 5]
#mista = ['python', 4, [1,2,3,4], True]
#print(len(mista))
#(python=0) (4=1) ([1,2,3,4]=2) (True=3)
#print(mista[0]) 
#linguagens = ['python', 'r', 'julia']
#linguagens.append('quibecru')
#print(linguagens)
#linguagens_adicionais = ['c++', 'java', 'javascript', 'sql']
#linguagens.extend(linguagens_adicionais)
#print(linguagens)
#linguagens[4] = 'coalhada'
#print(linguagens)
#linguagens.remove('javascript')
#print(linguagens)
#print(linguagens.pop())
#print(linguagens[0:-1:2])
