import sys

def fibonacciNoRecursivo(n: int) -> int:
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    
    actual, proximo = 0, 1
    i = 2
    while i <= n:
        actual, proximo = proximo, proximo + actual
        i += 1
    
    return proximo

if __name__ == '__main__':
  x = int(input())
  print(fibonacciNoRecursivo(x))
