#ej 9
"""
num = int(input("Ingrese num impar minimo 3 cifras: "))

largo = len(str(num))

print("")

ult = num%10
mid = (num//10**(largo//2))%10
pri = (num//10**(largo - 1))%10

print("El numero ingresado tiene",largo,"cifras")
print("La primera cifra es {}, la ultima es {}, y la central es {}".format(pri, ult, mid))
"""
#------------------------------------------------------------------------------
#ej10
"""
num = int(input("Ingrese un numero binario(max 5 bit): "))

d1 = (num//1)%10
d2 = (num//10)%10
d3 = (num//10**2)%10
d4 = (num//10**3)%10
d5 = (num//10**4)%10

num_dec = d1*2**0 + d2*2**1 + d3*2**2 + d4*2**3 + d5*2**4
print("Numero en decimal: ",num_dec)
"""
#-----------------------------------------------------------------
#ej11
"""
num = int(input("Ingrese un numero decimal(max 5 cifras): "))

d1 = (num//8**4)
d2 = (num//8**3)
d3 = (num%8**3)//(8**2)
d4 = ((num%8**3)%(8**2))//(8**1)
d5 = (((num%8**3)%(8**2))%(8**1))//(8**0)


num_octal = d5 + d4*10 + d3*10**2 + d2*10**3 + d1*10**4

print("")
print("Numero en octal: ",num_octal)
"""
#-----------------------------------------------------------------
#ej12
"""
num = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))
num3 = int(input("Ingrese el tercer numero entero: "))

suma = num + num2 + num3

print("{:=10d}".format(num))
print("{:=10d}".format(num2))
print("{:=10d}".format(num3))
print("----------")
print("{:=10d}".format(suma))

"""
#----------------------------------------------------------
# ej13
"""
num1 = int(input("Ingrese el multiplicado: "))
num2 = int(input("Ingrese el multiplicador: "))

m1 = num1 * (num2 % 10)
m3 = num1 * (num2 // (10**2))
m2 = num1 * ((num2 - ((num2 // (10**2)) *100)) //10) 

cuenta = num1 * num2

print("{:=10d}".format(num1))
print("x{:=9d}".format(num2))
print("----------")
print("{:=10d}".format(m1))
print("+{:=8d}-".format(m2))
print("{:=8d}--".format(m3))
print("----------")
print("{:=10d}".format(cuenta))

"""
#-----------------------------------------------------