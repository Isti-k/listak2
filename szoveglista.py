

'''1. Hány Alma/alma van a listában?'''
'''2. Hány Sz betűvel kezdődő szöveg van a listában?'''
'''3. Melyik a leghosszabb szó? Mekkora a hossza?
Hányadik heyen áll a listában?'''


#1. feladat:

def szamlalas(lista):
    print("1. feladat")
    db:int= 0
    for i in range(0, len(lista), 1):
        if lista[i].lower == "alma":
            db += 1
    return db

#2. feladat:

def Szamlalas2(lista):
    print("2. feladat")
    db:int=0
    for i in range(0, len(lista), 1):
        if lista[i][0:2] == "Sz":
            db += 1
    
    return db




