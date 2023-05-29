from typing import List

# Aclaración: Debido a la versión de Python del CMS, para el tipo Lista, la sintazis de la definición de tipos que deben usar es la siguiente:
# l: List[int]  <--Este es un ejemplo para una lista de enteros.
# Respetar esta sintaxis, ya que el CMS dirá que no pasó ningún test si usan otra notación.

def filasParecidas(matriz: List[List[int]]) -> bool :
    filas = len(matriz)
    columnas = len(matriz[0])

    patronGeneral = None
    for j in range(columnas):
        patronActual = matriz[1][j] - matriz[0][j]
        if patronGeneral is None:
            patronGeneral = patronActual
        elif patronActual != patronGeneral:
            return False

    for i in range(2, filas):
        for j in range(columnas):
            if matriz[i][j] - matriz[i-1][j] != patronGeneral:
                return None
    return patronGeneral

if __name__ == '__main__':
  filas = int(input())
  columnas = int(input())
 
  matriz = []
 
  for i in range(filas):         
    fila = input()
    if len(fila.split()) != columnas:
      print("Fila " + str(i) + " no contiene la cantidad adecuada de columnas")
    matriz.append([int(j) for j in fila.split()])
  
  print(filasParecidas(matriz))
