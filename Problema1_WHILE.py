#Se introduc succesiv numere nenule până la introducerea numărului 0. Să se afişeze suma tuturor numerelor introduse. 
suma=0
x=1
while x!=0:
    suma+=x
    x = eval(input('Introduceti numarul: '))

print(f'Suma numerelor introduse este {suma}')