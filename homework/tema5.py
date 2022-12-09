class Fractie:

    def __init__(self,numarator,numitor):
        self.numarator=numarator
        self.numitor=numitor

    def __str__(self):
        return f"{self.numarator}/{self.numitor}"


    def __add__(self,other):
        x= self.numarator * other.numitor +other.numarator * self.numitor
        y=self.numitor * other.numitor
        return Fractie(x,y)



    def __sub__(self,other):
        x = self.numarator * other.numitor - other.numarator * self.numitor
        y = self.numitor * other.numitor
        return Fractie(x, y)


    def inverse(self):
        x=self.numitor
        y=self.numarator
        return Fractie(x,y)














a=8
b=3
c=5
d=2
nr1=Fractie(a,b)
nr2=Fractie(c,d)

nr3=nr1+nr2
print(nr3)
nr3=nr1-nr2
print(nr3)
print(nr3.inverse())
