"""
recebendo dados do usuario

input -> todo dado recebido via input e String
david gomes
Em python String e tudo que etiver entre:
- aspas simples
- aspas duplas
- aspas simples triplas
- aspas duplas triplas

Exemplos:
- aspas simples -> 'david gomes'
- aspas duplas -> "david gomes"
- aspas simples triplas -> '''david gomes'''
- aspas duplas triplas -> """david gomes"""

"""
# Entrada de dados
# print("qual e o seu nome? ")
# nome = input()  #input significa entrada

nome = input("qual e o seu nome?")

# Exemplo do print antigo 2.x
#print("seja bem vindo(a) %s" %nome)

# Exemplo de print moderno 3.x
#print("seja bem vindo {}" .format(nome))

# Exemplo mais moderno possivel 3.7
#print(f"seja bem vindo {nome}")

#print("quantos anos vc tem? ")
#idade = input()

nome = int(input("qual e o seu nome?"))

# Processamento

# Saida de dados
print("a(o) %s tem %s anos" % (nome, idade))


# Exemplo de print mais atual 3.7
print(f"a(o) {nome} tem {idade} anos")
"""
# int(idade) => cast

Cast e o tipo de conversao de um dado para o outro

"""


print(f"a(o) {nome} nasceu em {2018 - int(idade)}")