conjunto = {"rojo", "azul", "blanco", "celeste"}
print(conjunto)
conjunto.add("Morado","Dorado")
print(conjunto)
conjunto.remove("celeste")
conjunto.remove("blanco")
conjunto.remove("Dorado")  
print(conjunto)

#ejercicio 2

lista_1 = [1, 2, 3, 4, 5]
lista_2 = [3, 4, 5, 6, 7]

lista_1_Set = set(lista_1)
lista_2_Set = set(lista_2)


variable = lista_1_Set.intersection(lista_2_Set)
print(variable)
