#Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative. 
s_p=s_n=nr_p=nr_n=0,0,0,0
l=1
while l<=12:
    t=eval(input('Introduceti temperatura lunii: '))
    if t>=0:
        s_p+=t
        nr_p+=1
    if t<0:
        s_n+=t 
        nr_n+=1
    l+=1

print(f'Media anuală a temperaturilor pozitive este {round(s_p/nr_p, 2)}, iar media anuală a temperaturilor negative este {round(s_n/nr_n, 2)}')   