#Unidad 2 Funciones
#Ej: 1
"""
def area(l1,l2,l3):#Parametros
    p = (l1 + l2 + l3)/2
    areatri = (p*(p-l1)*(p-l2)*(p-l3))**(1/2)
    #Otra cosa que podemos hacer es import math y desp poner math.sqrt

    return areatri #Esto hace que solo nos refiramos al area al hablar de la funcion

def main():#Siempre parentesis vacia
    l1 = int(input("Ingrese lado 1: ")) 
    l2 = int(input("Ingrese lado 2: ")) 
    l3 = int(input("Ingrese lado 3: ")) 

    fun = area(l1,l2,l3)
    
    print("El area del triangulo es = {:.2f}".format(fun))

main()
"""
#--------------------------------------------------------
#Ej: 2
"""
import math
def raiz(a,b):
    raiz = math.pow(a, 1/b)

    return raiz


def main():
    radicando = int(input("Ingrese el radicado (numero real): "))
    indice = int(input("Ingrese el indice (numero natural): "))

    fun = raiz(radicando,indice)

    print("La raiz {} de {} es = {:.6f}".format(indice,radicando,fun))

    
main()
"""
#--------------------------------------------------------
#Ej:3
"""
def paridad(num):
    d1 = (num//1)%10
    d2 = (num//10)%10
    d3 = (num//10**2)%10
    d4 = (num//10**3)%10
    d5 = (num//10**4)%10
    d6 = (num//10**5)%10
    d7 = (num//10**6)%10
    d8 = (num//10**7)%10
    
    suma = d1 + d2 + d3 + d4 + d5 + d6 + d7 + d8
    
    paridad = suma % 2
   
    return paridad

def main():
    num = int(input("Ingrese un numero de binario de hasta 8 bits: "))

    fun = paridad(num)
    print("Bit de paridad generado: {}".format(fun))
main()

"""    
#--------------------------------------------------------
#Ej: 4
"""
import math

def areaCirc(numcirc):
    area1 = ((numcirc/2)**2) * math.pi
    area2 = ((numcirc/2)**2) * math.pi
    area3 = ((numcirc)**2) * math.pi
    total = area1 + area2 + area3
    return total


def areaCuad(lado):
    areacuad = lado * lado
    return areacuad

def areaNegra(numcuad,numcirc):
    area = numcuad - numcirc
    return area
     
def main ():
    lado = int(input("Ingrese el lado: "))

    numcirc = areaCirc((lado)*(1/3)) 
    numcuad = areaCuad(lado)
    negra = areaNegra(numcuad,numcirc)

    porcentaje = (negra/numcuad)*100

    print("EL area negra es {:.2f} y es un {:.2f}% del area total del cuadrado".format(negra,porcentaje))

main()

"""
#--------------------------------------------------------
#Ej: 5
"""
import random
def incompleto (inferior,superior):
    primero = random.randint(inferior,superior)
    return primero

def medio (primer_adv,superior):
    segundo = random.randint(primer_adv,superior)
    return segundo

def completo (primer_adv,segunda_adv):
    tercero = random.randint(primer_adv,segunda_adv)
    return tercero

def main ():
    inferior = int(input("Ingrese el limite inferior (numero natural): "))
    superior = int(input("Ingrese el limite superior (numero natural): "))

    primer_adv = incompleto(inferior,(superior))
    segunda_adv = medio(primer_adv,(superior))
    tercera_adv = completo(primer_adv,segunda_adv) 

    print("1-Limite inferior {}, limite superior {}. Numerogenerado: {}".format(inferior,superior,primer_adv))
    print("2-Limite inferior {}, limite superior {}. Numerogenerado: {}".format(primer_adv,superior,segunda_adv))
    print("3-Limite inferior {}, limite superior {}. Numerogenerado: {}".format(primer_adv,segunda_adv,tercera_adv))

main()
"""
#Otra manera de hacerlo mas rapido
"""
import random
def azar (inferior,superior):
    azar = random.randint(inferior,superior)
    return azar

def main ():
    inferior = int(input("Ingrese el limite inferior (numero natural): "))
    superior = int(input("Ingrese el limite superior (numero natural): "))

    primer_adv = azar(inferior,superior)
    segunda_adv = azar(primer_adv,superior)
    tercera_adv = azar(primer_adv,segunda_adv)


    print("1-Limite inferior {}, limite superior {}. Numerogenerado: {}".format(inferior,superior,primer_adv))
    print("2-Limite inferior {}, limite superior {}. Numerogenerado: {}".format(primer_adv,superior,segunda_adv))
    print("3-Limite inferior {}, limite superior {}. Numerogenerado: {}".format(primer_adv,segunda_adv,tercera_adv))

main()
"""
#--------------------------------------------------------
#Ej:6
"""
import random

def azar(a,b):
    num = random.randint(0,1)
    return num

def main():
    v1 =  input("Ingrese alternativa 1 para vestimentas: ")
    v2 = input("Ingrese alternativa 2 para vestimentas: ")

    c1 =  input("Ingrese alternativa 1 de comida: ")
    c2 =  input("Ingrese alternativa 2 de comida: ")

    b1 = input("Ingrese alternativa 1 de bebida: ")
    b2 = input("Ingrese alternativa 2 de bebida: ")

    azar1 = azar(v1,v2)
    aleatoriaA = 1 - azar1

    azar2 = azar(c1,c2)
    aleatoriaB = 1 - azar2

    azar3 = azar(b1,b2)
    aleatoriaC = 1 - azar3

    vres = (azar1*v1) + (aleatoriaA*v2)
    cres = (azar2*c1) + (aleatoriaB*c2)
    bres = (azar3*b1) + (aleatoriaC*b2)

    print("Cena al azar: {}, {} y {}".format(vres, cres, bres))

main()
"""
#--------------------------------------------------------
#Ej: 7
"""
def string(fra,ancho):
    string = "'{0:>{1}}'".format(fra,(ancho-2))
    return string

def main():
    fra = input("Ingrese la frase: ")
    ancho = int(input("Ingrese el ancho total a ser usado: "))

    print(string(fra,ancho))

main()

"""
#--------------------------------------------------------
#Ej: 8
"""
def crearFila(ancho):
    string = "*" * ancho
    return string

def crearRectangulo(ancho,alto):
    rectangulo = (crearFila(ancho) + "\n") * alto
    return rectangulo
def main():
    ancho = int(input("Ingrese ancho: " ))
    alto = int(input("Ingrese alto: "))
    print(crearRectangulo(ancho,alto))
main()

"""