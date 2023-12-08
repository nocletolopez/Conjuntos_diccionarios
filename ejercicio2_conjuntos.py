#sets and dicts

elementos = {

    "paises": {

        "Inglaterra",
        "Usa",
        "México",        
    }

}

valores_a_añadir = {

        "Islandia",
        "Italia",
        "Argentina",
        "Portugal",
        "Usa"
}

elementos["paises"].update(valores_a_añadir)
print(elementos)

variable = {"Chile", "Usa"}
elementos["paises"].discard(variable)
print(elementos)


"""elementos["paises"].update({4:"Islandia"}) *forma de añadir utilizando update en dicts
print (elementos)"""
