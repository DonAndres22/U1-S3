import math as ma





def menu():
    print("Cosa vuoi calcolare tra quadrato, cerchio, rettangolo e fibonacci? ")
    q = input()
    if(q == "quadrato"):
        print("Lunghezza Lato: ")
        l = input()
        a, p = quadrato(l)
        print("Il perimettro è:", p, "L'area è:", a)
    elif(q == "rettangolo"):
        print("Lunghezza Base: ")
        b = input()
        print("Lunghezza Altezza: ")
        h = input()
        p, a = rettangolo(b, h)
        print("il perimetro è: ", p, "l'area è invece: ", a)
    elif(q == "cerchio"):
        print("raggio: ")
        r = input()
        c,a=cerchio(r)
        print("la circonferenza è: ", c, "l'area è invece: ", a)
    elif(q == "fibonacci"):
        print("Numero: ")
        n = input()
        fibonacci(n)
    else:
        print("input non corretto, puoi scegliere tra : <quadrato> <cerchio> <rettangolo> <fibonacci>")
        menu()
    print("Vuoi calcolare altro? y/n")
    c = input()
    if(c == "y"):
        menu()
    else:
        print("Grazie e arrivederci")






def quadrato(l):
    lato = float(l)
    p = lato * 4
    a = lato*lato
    return p, a


def cerchio(r):
    raggio = float(r)
    c = 2*ma.pi*raggio
    a = (ma.pi)*raggio**2
    return c, a

def rettangolo(b, h):
    base = float(b)
    alt = float(h)
    p = base*2 + alt*2
    a = base * alt
    return p, a

def fibonacci(b):
    num = float(b)
    l=[0,1]
    s=0
    while s<num:
        s=0
        for i in range(len(l)-2,len(l)):
            s=s+l[i]
        l.append(s)
    print(l)
    return l[0:len(l)-2]

menu()