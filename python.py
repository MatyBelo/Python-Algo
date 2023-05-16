def test(par):
    print("funciona")


def imprimirHola():
    print("hola")


def imprimirUnVerso():
    print("Never gonna give you up")
    print("Never gonna let you down")
    print("Never gonna run around")
    print("And desert you")



def esMultiploDe(x:int, y:int):
    if(x%y == 0):
        return (True)
    else:
        return (False)


def esMultiploRe(x:int, y:int) -> bool:
    if(x%y == 0):
        return True
    return False


def esMultiploDu(x:int, y:int):
    res: bool = False
    if(x%y == 0):
        res = True
    return res


def esMultiploDeGera(x:int, y:int) -> bool:
    return not(x%y)


def algunoEs0(x:int,y:int) -> bool:
    res: bool = False
    if(x == 0 or y == 0):
        res = True
    return res

def ambosSon0(x:int,y:int) -> bool:
    res: bool = False
    if(x == 0 and y == 0):
        res = True
    return res

def esNombreLargo(nombre: str) -> bool:
    res: bool = False
    if ((len(nombre) > 2) and (len(nombre) < 9)):
        res = True
    return res

def esBisiesto(ano: int) -> bool:
    res: bool = False
    if ((ano%4 == 0) and (not(ano%100 == 0))):
        res = True
    return res

def esBisiesto2(ano: int) -> bool:
    return((ano%4 == 0) and (not(ano%100 == 0)))



def esPar(numero:int) -> bool:
    return not(numero%2)

def devolverDobleSiEsPar(numero: int) -> int:
    res: int = numero
    if esPar(numero):
        res = numero * 2
    return res


'''

def numero710Veces ():
    return 
    while 

    return 

'''
def paresEntre10and40():
    i:int = 10
    while(i<=40):
        print(i)
        i = i+2


def paresEntre10y40():
    for i in range (10,40,2):
        print (i)


