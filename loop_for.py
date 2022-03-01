"""
Loop for

Loop -> Estrutura de repetição
for -> Uma dessas estruturas

C ou Java
for(int i = 0; i < 10; i++){
      //execução do loop
}

Python

for item in interavel:
    //execução do loop


Ultilizamos loops para interar sequências ou sobre valores iteráveis

Exemplos de iteráveis
- String
    nome = "David Gomes"
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = (1, 10)

range ( valor_inicial, valor_final )

obs:  o valor final nao é incluso
1
2
3
4
5
6
7
8
9
10 Não é incluso

nome = "David Gomes"
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista
# Exemplo de for 1 ( iterando sobre uma string )
for letra in nome:
    print (letra)

# Exemplo de for 2 ( iterando sobre uma lista )
for numero in lista:
    print (numero)

# Exemplo de for 3 ( iterando sobre um range )

for numero in range(1, 10):
    print(numero)

nome = "David Gomes"

lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista
# Exemplo de for 1 ( iterando sobre uma string )
for letra in nome:
    print (letra)
qtd = int(input("Quantas vezes esse loop vai rodar?"))
soma = 0
 for n in range (1, qtd+1):
     num = int(input(f"Informe o {n}/{qtd} valor: "))
     soma = soma = num
print(f"A soma é {soma}")
"""
