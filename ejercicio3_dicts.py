#ejercicio ingreso de datos(diccionario)
diccionario = {

    "nombre":None,
    "edad":None,
    "domicilio":None

}
nombre = input("Ingrese su nombre:  ")
edad = int(input("Ingrese su edad:  "))
direccion = input("Ingrese la dirección de su domicilio:  ")

diccionario["nombre"] = nombre
diccionario["edad"] = nombre
diccionario["domicilio v"] = nombre

variable = f"{diccionario[nombre]} tiene {diccionario[edad]}años y vive en{diccionario[direccion]}"
print(variable)