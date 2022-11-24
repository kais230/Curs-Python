def functie_1(param_1,param_2,*args,**kwargs):
   print(type(kwargs))
   suma=param_1+param_2
   for i in args:
       suma=suma+i

   return suma


print(functie_1(1,2,5,3,a=3,b=5))