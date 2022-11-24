# ex 1
def your_function(*args, **kwargs):
    suma=0
    for i in args:
        if type(i) == int or type(i) == float:
            suma += i
    return suma
# print(your_function(1, 5, -3 , "abc", [12,56,'cad']))



# ex 3
def citire():
    a = input("Adauga un numar: ")
    if a.isdigit() is True:
        return a
    else:
        return 0
