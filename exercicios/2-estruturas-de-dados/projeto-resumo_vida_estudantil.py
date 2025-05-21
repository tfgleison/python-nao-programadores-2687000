# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
estudante = {}

estudante['nome'] = input('Qual seu nome?: ')
estudante['ano_linkedin'] = int(input('Em qual ano conheceu o LinkedIn?: '))
estudante['ano_atual'] = int(input('Qual o ano atual?: '))
cursos = input('Quais cursos você já realizou no LinkedIn Learning?. Mencione do mais antigo para o mais recente, separados por vírgulas: ')

estudante['cursos'] = cursos.split(', ') 

# 2. Armazene esses dados em um dicionário
pessoa = {'nome': 'Gleison',
          'ano_inicio':2020,
          'ano_atual':2025,
          'cursos_linkedin': ['Análise de dados', 'Inteligência Artificial', 'Power BI', 'Inglês']}

# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
total_anos = estudante['ano_atual'] - estudante['ano_linkedin']
total_cursos = len(estudante['cursos'])

print(f"Olá {'nome'}. Fico feliz que você já nos conhece desde {'ano_linkedin'}. Seja bem vindo ao nosso curso de {'ano_atual'}. Legal que você já finalizou os cursos de: {'cursos_linkedin'}, sendo o primeiro deles: {estudante['cursos'][0]} e o último {estudante['cursos'][-1]}, seja bem-vindo novamente! ")

#split
#aluno = 'Gleison estuda Python'
#aluno.split()