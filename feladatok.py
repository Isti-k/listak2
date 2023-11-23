import math

'''1. Írj metódust, ami a paraméterben kapott lista elemeit kiírja a képernyőra'''

'''2. Mennyi a pozitív számok összege? - összegzés'''

'''3. Hány negatív szám van? - megszámlálás'''

'''4. Hány nem egész szám van a számok között? - megszámláls'''

'''5. Mennyi a hárommal osztható számok átlaga? - összegzés - megszámlálás'''

'''6. Mekkora a legnagyobb szám? - max'''

'''7. Mekkora a legkisebb szám - max'''

'''8. Mekkora a legkisebb és a legnagyobb szám külömbsége?'''



#1. feladat:

def kiiras(lista:int):
    print("1. feladat")
    for i in range(0, len(lista), 1):
        print(f"{i}. elem:{lista[i]}")


#2. feladat:

def pozitiv(lista:int):
    print("2. feladat")
    osszeges:int=0
    for i in range(0, len(lista), 1):
        if lista[i] > 0:
            osszeges += lista[i]
    
    return osszeges


#3. feladat:

def negativ(lista:int):
    print("3. feladat")
    db:int=0
    for i in range(0, len(lista), 1):
        if lista[i] > 0:
            db += 1
        
    
    return db


#4. feladat:

def szamlalas(lista:int):
    print("4. feladat")
    szamlalas:int=0
    for i in range(0, len(lista), 1):
        if round(lista[i]) != lista[i]:
            szamlalas += 1
        
    return szamlalas

#5. feladat:

def atlagolas(lista:int):
    print("5. feladat")
    osszeg:int=0
    atlag:int=0
    for i in range(0, len(lista), 1):
        if lista[i] % 3==0:
            osszeg += lista[i]
            atlag += 1
        
    return osszeg / atlag

#6. feladat:
def max(lista:int):
    print("6. feladat")
    max:int = lista[0]
    for i in range(0, len(lista), 1):
        if max < lista[i]:
            max = lista[i]

    return max

#7. feladat:
def min(lista:int):
    print("7. feladat")
    min:int = lista[0]
    for i in range(0, len(lista), 1):
        if min > lista[i]:
            min = lista[i]

    return min

#8. feladat:
def kulombseg(lista:int):
    print("8. feladat")
    max:int = lista[0]
    min:int = lista[0]
    for i in range(0, len(lista), 1):
        if min > lista[i]:
            min = lista[i]
        elif max < lista[i]:
            max = lista[i]

    return max-min







