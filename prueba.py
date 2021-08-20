#No lleva main y no hay ;
print("Hola mundo!")
#Declaraciones de variable de tipo inferido.
miNumero = 5
miNumero = 7.5
#Variables que cambian de tipo de dato
miNumero = "Siete punto cinco"
miNumero = "Ocho"
print("Mi número: " + str(miNumero))

a = 16
b = 80

#Condiciones
if a > b:
    print("A es mayor que B")
    print("Sigo estando en el bloque del if")
else: 
    print("A no es mayor que B")

print("Aquí ya estoy fuera del if")
#Ciclos
frutas = ["Manzana", "Sandia", "Melón", "Mango"]
for fruta in frutas:
    print("Fruta: "+fruta)
#Funciones
def mi_funcion():
    print("Estoy dentro de la función mi_funcion")
#Funciones con párametros
def saludar(nombre, apellidos):
    print("Hola " + nombre + " " + apellidos)

mi_funcion()
saludar("Azalia","Peña Hernández")
#saludar(input(),input())
