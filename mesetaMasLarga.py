from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintaxis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

def mesetaMasLarga(l: List[int]) -> int :
    masRepetido = None
    maximo = 0
    i = 0
    while i < len(l):
        numeroActual = l[i]
        conteoActual = 0
        j = 0
        while j < len(l):
            if l[j] == numeroActual:
                conteoActual += 1
            j += 1
        if conteoActual > maximo:
            maximo = conteoActual
            masRepetido = numeroActual
        i += 1
    return maximo
    

if __name__ == '__main__':
  x = input()
  print(mesetaMasLarga([int(j) for j in x.split()]))
