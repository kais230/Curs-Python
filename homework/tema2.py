# ex 1
def your_function(*args, **kwargs):
    sum=0
    for i in args:
        if type(i) == int or type(i) == float:
            sum += i
    return sum
# print(your_function(1, 5, -3 , "abc", [12,56,'cad']))



# ex 3
def citire():
    x = input("Adauga un numar: ")
    if x.isdigit() is True:
        return x
    else:
        return 0
