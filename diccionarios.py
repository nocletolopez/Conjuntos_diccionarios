#diccionario
base_de_datos = {
    "artículos": {

        "sal":10,
        "pan":20.0,
        "leche":25.5,
        "vino":100,
    },

    "proveedores":{

        1:"Sociedad",
        2:"Sociedad, el buen vino",
    },

}

print(base_de_datos)
"Obtengo el precio de la sal"
precio = base_de_datos["artículos"]["sal"]
print(precio)
proveedor = base_de_datos["proveedores"][1]
print(proveedor)