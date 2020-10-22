#Se citesc numere de la tastatură până la introducerea unui număr impar divizibil cu 3. Să se afişeze suma tuturor numerelor pare introduse.
x=0
s=0
while (x%2==0) or (x%3):
    x=eval(input('introduceti un numar: '))
    if x%2==0:
        s+=x

print('Suma tuturor numerelor pare introduse este ', s)