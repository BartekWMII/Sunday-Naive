import matplotlib.pyplot as plt
from random import choice

counter = 0

#pomocnicza tablica do sunday'a
shift = {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1, 'f': -1, 'g': -1, 'h': -1, 'i': -1,
         'j': -1, 'k': -1, 'l': -1, 'm': -1, 'n': -1, 'o': -1, 'p': -1, 'r': -1, 's': -1,
         't': -1, 'u': -1, 'w': -1, 'x': -1, 'y': -1, 'z': -1}
#alfabet
A = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
     'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'x', 'y', 'z']

#alfabet specjalny w przypadku zmiennej dlugosci alfabetu
Z = ['a', 'd', 'e', 'f', 'g', 'l', 'm', 'n', 'o', 'u', 'w', 'x', 'y', 'z']

#PORÓWNUJE WZORZEC I TEKST, ZLICZA LICZBE PORÓWNAŃ, P TO NASZE MIEJSCE W TEKŚCIE KTORE PORÓWNUJEMY
def matchesAt(T, W, p):
    global counter
    for i in range(len(W)):
        counter = counter + 1
        if T[p + i] != W[i]:#PORÓWNUJE TEKST DO WZORCA
            return False
    return True

#SPRAWDZA CZY WZORZEC WYSTEPUJE W TEKSCIE DLA WSZYSTKICH KOLEJNYCH POZYCJI P
def naiveSearch(T, W):
    result = []
    global counter
    counter =0# ZLICZANIE POROWNAN
    for p in range(len(T) - len(W) + 1):
        if matchesAt(T, W, p):
            result.append(p)
    return result


def rand_text(A, l):
    result = ""
    for _ in range(l):
        result += choice(A)
    return result


def Sunday(T, W, zm):
    result = []
    global counter
    counter =0 #ZLICZAMY POROWNANIA
    p = 0 #NASZA POZYCJA

    for i in range(len(W)): #ZAPISUJEMY W TABLICY SHIFT OSTATNIE WYSTAPIENA LITER ( ICH INDEKSY)
        zm[W[i]]=i

    while p <= len(T) - len(W): #DOPÓKI NASZA POZYCJA JEST MNIEJSZA OD |T| - |W|
        if (matchesAt(T, W, p)):#JESLI MATCHESAT ZWROCI PRAWDE TO DODAJEMY POZYCJE DO TABLICY
            result.append(p)
        p = p + len(W) #ZWIEKSZAMY P O DLUGOSC WZORCA
        if p < len(T):#JESLI P < |T|
            p = p - zm[T[p]]#P ZMNIEJSZAMY O LICZBE W TABLICY SHIFT ( LUB ZWIEKSZAMY O 1)
    return result

## ALG W ZAELEZNOSCI OD DLUGOSSCI TEKSTU
def alg1(A):
    W = ""
    W += rand_text(A, 5)
    T = ""
    X = []
    Y = []
    YY = []
    last=shift.copy()
    for _ in range(1000):
        T += rand_text(A, 5)
        X.append(len(T))
        naiveSearch(T, W)
        Y.append(counter)
        Sunday(T, W,last)
        YY.append(counter)
    return X, Y, YY

## ALG W ZALEZNOSCI OD DLUGOSCI WZORCA
def alg2(A):
    T = rand_text(A, 10000)
    W = ""
    X = []
    Y = []
    YY = []
    last=shift.copy()
    for _ in range(35):
        W += rand_text(A, 1)
        X.append(len(W))
        naiveSearch(T, W)
        Y.append(counter)
        Sunday(T, W, last)
        YY.append(counter)
    return X, Y, YY

#ALG W ZALEZNOSCI OD DLUGOSCI WIELKOSCI ALFABETU
def alg3(Z):
    C=[]
    X=[]
    Y=[]
    YY=[]
    last = shift.copy()
    for i in range(len(Z)):
        C+= Z[i]
        T = rand_text(C, 10000)
        W = rand_text(C, 10)
        X.append(len(C))
        naiveSearch(T,W)
        Y.append(counter)
        Sunday(T, W, last)
        YY.append(counter)
    return X, Y, YY

#FUNKCJA DO WYSWIETLENIA WYKRESOW
def show(var):
    if var == 'A':
        g = alg1(A)
        plt.xlabel("Długość Tekstu")
        plt.plot(g[0], g[1], label="Naive")
        plt.plot(g[0], g[2], label="Sunday")
    if var == 'B':
        gg = alg2(A)
        plt.xlabel("Długość Wzorca")
        plt.plot(gg[0], gg[1], label="Naive")
        plt.plot(gg[0], gg[2], label="Sunday")
    if var == 'C':
        ggg = alg3(Z)
        plt.xlabel("Długość alfabetu")
        plt.plot(ggg[0], ggg[1], label="Naive")
        plt.plot(ggg[0], ggg[2], label="Sunday")
    plt.ylabel("Liczba porównań")
    plt.title("Porównanie naiwnego i Sunday'a")
    plt.legend()
    plt.show()

#WYWOLANIE WYKRESOW
show('A')
show('B')
show('C')
