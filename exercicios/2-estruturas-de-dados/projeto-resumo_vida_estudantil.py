# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.


nome = input("Qual é o seu nome? ")
ano_conheceu_linkedin = int(input("Em que ano você conheceu o LinkedIn? "))
ano_atual = int(input("Em que ano estamos? "))
cursos_realizados = input(
    "Quais cursos você realizou no LinkedIn Learning? (separados por vírgula) "
)

cursos_realizados_lista = cursos_realizados.split(", ")

estudante = {
    "nome": nome,
    "ano_conheceu_linkedin": ano_conheceu_linkedin,
    "ano_atual": ano_atual,
    "cursos_realizados": cursos_realizados_lista,
}

anos_transcorridos = estudante["ano_atual"] - estudante["ano_conheceu_linkedin"]
total_cursos = len(estudante["cursos_realizados"])

print(
    f"{estudante['nome']} conheceu o LinkedIn em {estudante['ano_conheceu_linkedin']}, ou seja, há {anos_transcorridos} anos. Ela realizou um total de {total_cursos} cursos, sendo o primeiro '{estudante['cursos_realizados'][0]}' e o último '{estudante['cursos_realizados'][-1]}'."
)