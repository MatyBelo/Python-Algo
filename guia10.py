# readline(): Lee y devuelve la línea del archivo.

# readlines(): Lee todas las líneas del archivo y las devuelve como una lista.


def contarlineas(archivo: str) -> int:
    
    contenido = archivo.readlines()
    
    cantidadLineas: int = 0
        
    for i in range(0,len(contenido),1):
        if (archivo.readline(i) == ""):
            cantidadLineas += 1

    return cantidadLineas

print(contarlineas(open("neva.txt","r")))


def existePalabra(palabra : str, archivo : str) -> bool:

    contenido = archivo.readlines()

    for i in range(0,len(contenido),1):
        if palabra in (contenido[i]):
            return True
    return False 

print(existePalabra("goodbye",open("neva.txt","r")))



def cantidadApariciones(archivo : str, palabra : str) -> int:
    
    cantidadPalabra: int = 0

    contenido = archivo.readlines()

    for i in range(0,len(contenido),1):
        linea = list(contenido[i].split())
        for j in range(len(linea)):
            if (linea[j] == palabra):
                cantidadPalabra += 1
    return cantidadPalabra

print(cantidadApariciones(open("neva.txt","r"),"Never"))
