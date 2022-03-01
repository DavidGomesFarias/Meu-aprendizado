"""
Ranges

- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com os loops for.

Ranges são usados para gerar sequências numéricas, não de forma aleatória,
mas sim de maneira especificada.

Formas gerais:

# Forma 1

range(valor_de_parada)

OBS: valor_de_parada não inclusive (valolr_inicio padrão 0, e passo de 1 em 1)

# Exemplo Forma 1
for num in range(11):
    print(num)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (valor_inicio especificado pelo usuário, e passo de 1 em 1)

# Exemplo Forma 2
for num in range(1,11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (valor_inicio especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo Forma 3
for num in range(0, 55, 5):
    print(num)

# Forma 4 (inversa)

range(valor_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (valor_inicio especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo Forma 4
for num in range(10, -1, -1):
    print(num)
"""

