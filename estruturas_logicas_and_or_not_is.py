"""
Estruturas Logicas
and (e), or (ou), not (não), is (é)

operadores unarios:
    - not
operadores binarios:
    - and, or, is

Regras de funcionamento:

para o "and" ambos os valores precisam ser True
para o "or" um ou outro valor precisa ser True
para o "not" o valor do booleano é invertido, ou seja, se for True vira False e se for False vira True
para o "is" o valor e comparado com um segundo
"""
ativo = True
logado = False

if ativo:
    print("voce precisa ativar a sua conta, por favor cheque o seu e-mail")
else:
    print("Bem-vindo usuario!")

# ativo e falso?
print(ativo is True)

