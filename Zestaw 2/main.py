#Dominik Juszczyk

#Zadanie 2.10
line = "Phasellus placerat\tvehicula consequat.\nDuis GvR sodales \tlorem.\nAenean quis."
lista = line.split()
print("Zadanie 2.10\n\t", len(lista), "\n")


#Zadanie 2.11
word = "word"
print("Zadanie 2.11\n\t" + "_".join(word) + "\n")


#Zadanie 2.12
print("Zadanie 2.12\n  a)\n\t" + "".join(x[0] for x in lista))
print("  b)\n\t" + "".join(x[-1] for x in lista) + "\n")


#Zadanie 2.13
print("Zadanie 2.13\n\t", sum(len(x) for x in lista), "\n")


#Zadanie 2.14
najdluzszyWyraz = 0
wyraz = ""
for x in lista:
    if len(x) > najdluzszyWyraz:
        najdluzszyWyraz = len(x)
        wyraz = x
print("Zadanie 2.14\n  a)\n\t" + wyraz + "\n  b)\n\t", najdluzszyWyraz, "\n")


#Zadanie 2.15
L = [5, 23, 632, 63, 7, 8, 2, 5, 6, 14, 2, 0, 9, 1]
ciagCyfr = " ".join(str(x) for x in L)
print("Zadanie 2.15\n\t" + ciagCyfr + "\n")


#Zadanie 2.16
newLine = line.replace("GvR", "Guido van Rossum")
print("Zadnie 2.16\n\t", newLine, "\n")


#Zadanie 2.17
sortedLine = sorted(line.split(), key=str.lower)
print("Zadanie 2.17\n\t", sortedLine)
sortedLine = sorted(line.split(), key=len)
print("\t", sortedLine, "\n")


#Zadanie 2.18
liczbaCalkowita = 1230456078090
liczbaCalkowita = str(liczbaCalkowita)
licznik = 0
for x in range(len(liczbaCalkowita)):
    if liczbaCalkowita[x] == '0':
        licznik = licznik + 1
print("Zadanie 2.18\n\t", licznik, "\n")


#Zadanie 2.19
listaCyfr = " ".join(str(x).zfill(3) for x in L)
print("Zadanie 2.19\n\t", listaCyfr, "\n")
