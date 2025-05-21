# Criaremos um programa para substituir números por palavras em uma lista
# 1. Crie uma lista com 15 números

lista_numerica = list(range(15,31))
print(lista_numerica)
#[15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

# 2. Crie um for loop para percorrer todos os elementos da lista
indice = 0
for numero in lista_numerica:
  if numero % 3 == 0: and numero % 5 == 0:
    lista_numerica[indice] = 'FizzBuzz'
  elif numero % 3 == 0:
    lista_numerica[indice] = 'Fizz'  
  elif numero % 5 == 0:
    lista_numerica[indice] = 'Buzz'
  else:
    lista_numerica[indice] = numero  
  indice += 1

print(lista_numerica)


# 3. Crie uma estrutura condicional para verificar cada número da lista:
# 3.1 Caso o número seja divisível por 3, substitua-o por "Fizz"
# 3.2 Caso o número seja divisível por 5, substitua-o por "Buzz"
# 3.3 Caso o número seja divisível por 3 e 5, substitua-o por "FizzBuzz"

