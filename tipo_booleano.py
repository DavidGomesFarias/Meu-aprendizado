"""
Tipo Booleano

algebra booleana, cirada por george boole

2 constantes, verdadeiro ou falso

True -> verdadeiro

False -> falso

sempre com a inicial maiuscula

errado: true, false

certo: True, False


"""

ativo = True

print(ativo)

# Negação (not) :

"""

fazendo a negacao , se o valor booleano for verdadeiro o resultado sera falso, e se for falso o resultado sera 
verdadeiro ou seja sempre ao contrario.
"""

print(not ativo)

# Ou (or)

"""

e uma operacao binaria, ou seja depende de dois valores ou um ou outro deve ser verdadeiro

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
logado = False
print(ativo or logado)

# E (and) :
"""
tambem e uma operacao binaria, ou seja, depende de dois valores e ambos os valores devem ser verdadeiros

True and True -> True
True and False -> False
False and True -> False 
False and False -> True
"""
