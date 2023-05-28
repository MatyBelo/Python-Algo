import sys

def fibonacciNoRecursivo(n: int) -> int:
    secuencia = []
    if n >= 1:
        secuencia.append(0)
    if n >= 2:
        secuencia.append(1)
    while secuencia[-1] + secuencia[-2] <= n:
        secuencia.append(secuencia[-1] + secuencia[-2])
    return secuencia


if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))
