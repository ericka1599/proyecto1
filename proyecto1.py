#Problema 1
def prob_1 (n):
    if n % 2 == 0: 
        return True
    else:
         return False

a = int(input("Deme un entero: "))

print (prob_1(a))

#Problema 2 
def prob_2 (f):
    r = (f - 32) * 0.5555
    print (r)

b = int(input("Ingrese grados en Farenheight: "))
print (prob_2(b))


#Problema 3
def Prob_3 (bn, pn):
    c = 0
    if c < pn:
        r = bn * bn
        c = c + 1
    print (r)
    
bn = int(input("Deme la base: "))
pn = int(input("Deme la potencia: "))
print (Prob_3 (bn,pn))


#Problema 4
def Prob_4 (hil, lon): 
    hilL = len(hil)
    re = lon - hilL
    re = int(re)
    div = re / 2
    divn = int(div)
    print('*' * divn + hil + '*' * divn ) 

e = input("Ingrese la hilera de caracteres: ")
f = int(input("Ingrese la longitud del parrafo: "))
print (Prob_4(e, f))



#Problema 5 
def prob_5 (im, jm, km, idn, jn, kn ):

    I = ((jm * kn) - (km * jn))
    Ies = str(I)
    J = - ((im * kn) - (km * idn))
    Jes = str(J)
    K = ((im * jn) - (jm * idn))
    KA = str(K)

    print ( Ies + "I-" + Jes + "J+" + KA)

im = int(input("Ingrese i de m: "))
jm = int(input("Ingrese j de m: "))
km = int(input("Ingrese k de m: "))

idn = int(input("Ingrese i de n: "))
jn = int(input("Ingrese j de n: "))
kn = int(input("Ingrese k de n: "))

print (prob_5(im, jm, km, idn, jn, kn))


#Problema 6 
def Prob_6 (alist):
    for passnum in range (len(alist)-1, 0, -1):
        for i in range (passnum):
            if alist[i] > alist [i + 1]:
                temp = alist [i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = []
cont = 0
ans = int(input("Cuantos numeros va a ingresar? "))
while ans > cont:
    alist.append(int(input("Ingresa: ")))
    cont = cont + 1
Prob_6(alist)
print(alist)

#Problema 7
def prob_7
print ("Los multiplos de 4 son: ")
for i in range (0, 1000, 4):
        print (i)

# Problema 8
def prob_8 (num):

        cont = num 
        veces = 0
        while cont > 0:
                cont = cont - 1
                veces = veces + 1
                midcont = cont - veces
                print (" " * cont + "* " * veces + " ") 


num = int(input("Ingrese el altura: "))
print(prob_8(num))

#Problema 9
def Prob_9 (a, b, c):


    if a > b and a > c :
        if b**2 + c**2 == a**2 :
            print ("Si es una tripleta pitagorica")
        else:
                print ("No es una terna pitagorica")
    elif b > a and b > c :
        if a**2 + c**2 == b**2 :
            print ("Si es una tripleta pitagorica")
        else:
                print ("No es una terna pitagorica")
    elif c > a and c > b :
        if a**2 + b**2 == c**2 :
            print ("Si es una tripleta pitagorica")
        else:
                print ("No es una terna pitagorica")

            
print ("tripletas pitagoricas")
a = int(input("Ingresa a: "))
b = int(input("Ingresa b: "))
c = int(input("Ingresa c: "))
print(Prob_9(a, b, c))



#Problema 11
def Prob_11 (frase):
 
    temp = frase.replace(' ','')
    
    if temp == temp[::-1]: 
        print('La frase es palindromo') 
    else: 
        print('No es palindromo') 

frase = input('Ingrese una frase toda en minusculas: ')
print (Prob_11(frase))

def prob_18 (num):
    lista = [0, 1]
    cont = 1
    suma = 1

    while cont <= num :
        ant = (lista[cont - 1] )
        antant = (lista[ant - 1])
        suma = ant + suma
        cont = cont + 1 
        lista.append(suma)

    if num == lista :
        print ("Si es parte de la serie de Fibonacci")
    else :
        print ("No es parte de la serie de Fibonacci")
        
    return lista

num = int(input("Ingrese el numero: "))
print (prob_18(num))