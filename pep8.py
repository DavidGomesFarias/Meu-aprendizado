"""
PEP8 - Python Enhancement Proposital

sao propostas demelhoria para o python

the zen of python

import this

a ideia da pep8 e que possamos escrever codigos python de forma pythonica

1 - ultilize camel case para nomes de classes
class Calculadora:
    pass


class CalculadoraCientifica:
    pass

2 - Ultilize nomes em minusculo, separados por _ pora funcoes ou variaveis
def soma()
    pass

def soma_dois()
    pass

numero =4

numero_impar = 5

3 - Ultilize 4 espaços para identação! (nao use o tab)
if "a" in "banana" :
    print("tem")

4 - linhas em branco
- separar funcoes e definicoes de classes com duas linhas em branco
- metodos dentro de uma classe devem ser separados com uma unica linha em branco

class Classe:
    pass


class Outra:
    pass

5 - imports
- imports sempre devem ser feitos em linhas separadas:
#import errado

import sys, os

#import certo

import sys
import os

#nao ha problemas em ultilizar:

from types StringType, ListType

#caso tenha muitos imports do mesmo pacote, recomenda-se fazer:

from types import (
    StringType
    ListType
    SetType
    Outrotype
)


# Imports devem ser colocados no topo no arquivo logo depois de quaisquer comentarios ou doc Strings e
# antes de constantes ou variaveis globais

6 - espaços em expressões e instruções
# não faça

função (algo[ 1 ], { outro: 2 } )


# faça

função(algo[1], {outro: 2

# não faça

algo (1)

# faça

algo(1)

7 - Termine sempre uma instrução com uma nova linha
"""
import this
