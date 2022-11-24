a = 2
'''
def functie():
    mesaj ="Buna seara"
    print(mesaj)


functie()
'''

def functie():
    def functie2():
        print(f"A doua functie: {msg}")
    global msg
    msg ="Buna seara"
    functie2()
    print(f"functie: {msg}")




functie()
msg="Buna ziua"
print(msg)