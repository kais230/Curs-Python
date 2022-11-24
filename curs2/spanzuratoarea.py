# cuvant = ' o n o m a t o p e e'
"""
daca litera de inceput si litera de sfarsit se gasesc in interiorul cuvantului, litera
trebuie sa fie vizibila

cuvant = 'o _ o _ _ _ o _ e e'
7 incercari
"""

cuvant_de_ghicit = 'onomatopee'.lower()
cuvant = list('onomatopee')
litere_incercate = set()

for index, valoare in enumerate(cuvant):
    # print(cuvant[0], cuvant[-1])
    if cuvant[0] != valoare and cuvant[-1] != valoare:
        cuvant[index] = '_'

# print(cuvant)
cuvant_de_afisat = ' '.join(cuvant)

"""
sa nu fie cifra string.isdigit()
sa nu introduca mai mult de 1 caracter len(string) > 1
si sa nu fie spatiu litera_de_incercat in ["", " "]
"""

numar_incercari = 0

while numar_incercari < 7:

    if len(list(litere_incercate)) > 0:
        print(f"Literele incercate sunt {','.join(litere_incercate)}")

    litera_de_incercat = input("Adauga o litera: ").lower()

    while not litera_de_incercat.isalpha() or len(litera_de_incercat) > 1 or litera_de_incercat in ["", " "]:
        if not litera_de_incercat.isalpha():
            print(f"Te rugam sa adaugi o litera. ")
        elif len(litera_de_incercat) > 1:
            print(f"Ai daugat mai multe caractere. Ai voire sa adaugi un singur caracter.")
        elif litera_de_incercat in ["", " "]:
            print("Ai adaugat un spatiu. Te rugam sa introduci un caracter")
        litera_de_incercat = input("Adauga o litera: ").lower()

    if litera_de_incercat not in cuvant_de_ghicit:
        numar_incercari += 1
        litere_incercate.add(litera_de_incercat)
    elif litera_de_incercat in cuvant_de_ghicit and (cuvant_de_ghicit[0] != litera_de_incercat and cuvant_de_ghicit[-1] != litera_de_incercat):

        for index,valoare in enumerate(cuvant_de_ghicit):
            if valoare == litera_de_incercat:
                cuvant[index] = litera_de_incercat

    if '_' not in cuvant:
        print("Ai castigat")
        break
    elif numar_incercari == 7:
        print(f"Ai pierdut. Cuvantul initial era {cuvant_de_ghicit}")
    else:
        print(f"Mai ai {7 - numar_incercari} incercari")
    print(" ".join(cuvant))