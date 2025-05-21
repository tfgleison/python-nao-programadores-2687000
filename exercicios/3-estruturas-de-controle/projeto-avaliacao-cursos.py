# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.

# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
cursos_linkedin = ['SQL', 'Python', 'Power BI', 'Análise de dados', 'DP-900']

# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
curso_basic = 'SQL'
curso_inter = 'Power BI'
curso_hard = 'Python'

# 3. Crie um dicionário vazio para armazenar a nota do curso
avaliações = {}

# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
if curso_basic in cursos_linkedin:
  print(f"O curso {curso_basic} está presente na grade. Por favor, avalie o curso.")
avaliações[curso_basic] = int(input('Qual é a nota que você dá para o curso? (0 a 5): '))

if curso_inter in cursos_linkedin:
  print(f"O curso {curso_basic} está presente na grade. Por favor, avalie o curso.") 
avaliações[curso_inter] = int(input('Qual é a nota que você dá para o curso? (0 a 5): '))    

if curso_hard in cursos_linkedin:
  print(f"O curso {curso_basic} está presente na grade. Por favor, avalie o curso.")
avaliações[curso_hard] = int(input('Qual é a nota que você dá para o curso? (0 a 5): '))  

# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota
print(avaliações)
