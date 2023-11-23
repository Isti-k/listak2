szam_lista=[12, 23, -56, 82, 12.23, 69, -100]
szoveg_lista=["Alma","Körte","Szilva","Szőlő","alma"]
import feladatok
import szoveglista

feladatok.kiiras(szam_lista)

p=feladatok.pozitiv(szam_lista)
print(f"Pozitív számok száma:{p}")
print()

n=feladatok.negativ(szam_lista)
print(f"Negatí számok száma:{n}")
print()

sz=feladatok.szamlalas(szam_lista)
print(f"Számok száma:{sz}")
print()

a=feladatok.atlagolas(szam_lista)
print(f"Az átlag száma:{a}")
print()

max=feladatok.max(szam_lista)
print(f"Legnagyobb szám:{max}")
print()

min=feladatok.kulombseg(szam_lista)
print(f"Legkisebb szám:{min}")
print()

sza=szoveglista.szamlalas(szoveg_lista)
print(f"Ennyi van benne:{sza}")
print()

sza2=szoveglista.szamlalas(szoveg_lista)
print(f"Ennyi van benne:{sza2}")
print()


