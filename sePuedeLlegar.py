from typing import List
from typing import Tuple

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista y Tupla, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# t: Tuple[str,str]  <--Este es un ejemplo para una tupla de strings.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

def sePuedeLlegar(origen: str, destino: str, vuelos: List[Tuple[str, str]]) -> int:
    listaVuelos = []
    for vuelo in vuelos:
        ciudadOrigen, ciudadDestino = vuelo
        listaVuelos.append((ciudadOrigen, ciudadDestino))

    queue = [(origen, 0)]
    visitados = set()

    while queue:
        ciudadActual, numDeVuelos = queue.pop(0)

        if ciudadActual == destino:
            return numDeVuelos

        visitados.add(ciudadActual)

        for vuelo in listaVuelos:
            ciudadOrigen, ciudadDestino = vuelo
            if ciudadOrigen == ciudadActual and ciudadDestino not in visitados:
                queue.append((ciudadDestino, numDeVuelos + 1))
    
    return -1

if __name__ == '__main__':
  origen = input()
  destino = input()
  vuelos = input()
  
  print(sePuedeLlegar(origen, destino, [tuple(vuelo.split(',')) for vuelo in vuelos.split()]))
