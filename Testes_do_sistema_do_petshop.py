nome = str(input("Olá, Qual é o seu nome? "))
print(str(f"Olá {str.title(nome)} Seja Bem-vindo(a) "))

escolha = int(input("Vamos falar sobre Gato ( 1 ) ou Cachorro ( 2 )? "))

Gato = 1
Cachorro = 2

Banho = 1
Higiene: int = 2

# Gato

if escolha < 2:
    print("Ok, qual é a sua dúvida? ")
    Banho = int(input("( 1 Sim ou 2 Não ) Banho com Shampoo/Condicionador? "))
    if Banho == 1:
        print("O nosso banho e feito com Shampoo e Condicionador, com o maximo de cuidado possivel com o seu gato(a)\n"
              "colocamos algodão no ouvido dele(a) para não entrar agua, a nossa agua é morna ( não tão quente e\n"
              "não tão fria ), e ao final do banho secamos ele com secador de cabelo em temperatura ambiente e tambem"
              "\npenteamos ele para ficar lindo esperando você, caso você queira podemos colocar lacinhos nele(a). ")
    else:
        print("Ok")

    Higiene = int(input("( 1 Sim ou 2 Não ) Higiene: Limpeza do ouvido e corte de unhas? "))
    if Higiene == 2:
        print(
            "Nos limpamos o ouvido do seu gato(a) com cotonetes e com todo o cuidado do mundo para não machucar o seu\n"
            "pet,cortamos a unha e lichamos para não ficar arranhando e ficar linda.")
    else:
        print("Ok")

    Duvida: str = str(input("Todas as suas dúvidas foram respondidas? (Sim ou Não)"))
    if Duvida == "sim":
        print("Perfeito, muito obrigado pela preferência.")
    else:
        print("Ligue para o nosso número (00)00000-0000 e fale conosco.")

# Cachorro

Banho = 1
Higiene = 2

if escolha > 1:
    print("Ok, qual é a sua dúvida? ")
    Banho = int(input("( 1 Sim ou 2 Não ) Banho com Shampoo/Condicionador e com ou sem tosa? "))
    if Banho == 1:
        print(
            "O nosso banho e feito com Shampoo e Condicionador, com o maximo de cuidado possivel com o seu\n"
            "cachorro(a), colocamos algodão no ouvido dele(a) para não entrar agua, a nossa agua é morna\n"
            "( não tão quente e não tão fria ), e ao final do banho secamos ele com secador de cabelo em temperatura\n"
            "ambiente e tambem penteamos ele para ficar lindo esperando você, se você quiser tambem podemos tosar\n"
            "ele e caso você queira podemos colocar lacinhos nele(a). ")
    else:
        print("Ok")

    Higiene = int(input("( 1 Sim ou 2 Não ) Higiene: Limpeza do ouvido e corte de unhas? "))
    if Higiene == 1:
        print(
            "Nos limpamos o ouvido do seu Cachorro(a) com cotonetes e com todo o cuidado do mundo para não machucar \n"
            "o seu pet, cortamos a unha e lichamos para não ficar arranhando.")
    else:
        print("Ok")

    Duvida = str(input("Todas as suas dúvidas foram respondidas? (Sim ou Não)"))

    if Duvida == "sim":
        print("Perfeito, muito obrigado pela preferência.")
    else:
        print("Ligue para o nosso número (00)00000-0000 e fale conosco.")
