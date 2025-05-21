# Crie duas variáveis do tipo numérica, uma sinalizando a fase atual do curso e outra o nível final
# Insira "else" no while loop anterior.

nivel_atual = 1
nivel_final = 4

while nivel_atual <= nivel_final:
  print(f'Você avançou um nível do curso. Seu nível atual é {nivel_atual}.')
  nivel_atual += 1
else:
  print('Parabéns! Você concluiu o curso.')