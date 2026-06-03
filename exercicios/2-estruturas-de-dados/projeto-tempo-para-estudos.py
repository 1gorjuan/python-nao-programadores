# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:

# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input("Digite o seu nome: ")

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = input("Digite o total de dias dedicados ao estudo por semana: ")

# 3. Crie uma variável chamada "total_horas" e, usando o método input(), solicite a média de horas estudada por dia;
total_horas = input("Digite a média de horas estudada por dia: ")

# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input("Digite o título do curso desejado: ")

# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print(
    f"{nome} dedicou {total_dias} dias na semana, estudando {total_horas} horas por dia, para o curso de {curso}."
)
