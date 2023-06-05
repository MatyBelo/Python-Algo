

def contarlineas(archivo: str) -> int:
    
    archivo = open("neva.txt","r")

    contenido = archivo.readlines()
    
    cantidadLineas = 0
        
    for i in range(0,len(contenido),1):
        if (readline(i) == " "):
            cantidadLineas += 1

    archivo.close()

    return cantidadLineas



# readline(): Lee y devuelve la línea del archivo.

# readlines(): Lee todas las líneas del archivo y las devuelve como una lista.




# def existePalabra(palabra : str, archivo : str) → bool
