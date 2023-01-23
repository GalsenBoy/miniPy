def addition():
    try:
        x = int(input("Veuillez saisir le premier nombre" + "\n"))
        y = int(input("Veuillez saisir le second nombre" + "\n"))
        while type(x) != int and type(y) != int:
            x = int(input("Veuillez saisir le premier nombre" + "\n"))
            y = int(input("Veuillez saisir le second nombre" + "\n"))
    except:
        print("Veuillez saisir des nombres valide")

    else:
        return x + y

def soustraction(x, y):
    return x-y

def mult(x, y):
    return x*y

def div(x,y):
    try:
        return x / y
    except:
        print("Division avec 0 impossible")

print(addition())