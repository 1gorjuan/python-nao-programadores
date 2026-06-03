pessoa = {'nome':'Crislaine', 
          'idade':46, 
          'ano_formatura':2010, 
          'linguagens_programacao':['python', 'r', 'javascript', 'ruby'], 
          'brasileira':True, 
          'hobby':['nadar', 'ler', 'pedalar'], 
          'animal_estimacao':False}

# Imprima na tela o valor equivalente a chave "hobby"

print(pessoa['hobby'])

# Imprima na tela uma lista apenas com os valores do dicionário
print(list(pessoa.values()))

# Imprima na tela uma lista apenas com as chaves do dicionário

print(list(pessoa.keys()))
# Insira um novo par chave-valor no dicionário

pessoa['profissao'] = 'Analista de Dados'