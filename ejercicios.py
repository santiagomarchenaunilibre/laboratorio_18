print("raices de un polinomio ax^2+bx+c")
a= int(input("ingresa el valor de a: "))
print(a)
b= int(input("ingresa el valor de b: "))
print(b)
c= int(input("ingresa el valor de c: "))
print(c)
rq= (b**2-(4*(a*c)))**(1/2)
r1= (-b+(rq))/2*a
r2= (-b-(rq))/2*a
print("el valor de la R1 es ",r1)
print("el valor de la R2 es ",r2)
#-----------------------------------------------------------------------------
t = float(input("Ingrese temperatura en grados Celsius: "))
k = t + 273.15
print("La temperatura en grados Kelvin es:",k)

#-----------------------------------------------------------------------------
print("temperatura en °F")
c= float(input("ingresa la temperatura en °c: "))
f= ((c*9)/5)+32
print("el valor de la temperatura °F es:",f)
 
print("temperatura en °c")
f= float(input("ingresa la temperatura en °F: "))
c= ((f-32)*5)/9
print("el valor de la temperatura °c es:",c)

#-----------------------------------------------------------------------------
nombre = (input("Por favor, ingrese su nombre: "))
edad = int(input("Por favor, ingrese su edad: "))
print("Su nombre es:",nombre)
print("Su edad es:",edad)