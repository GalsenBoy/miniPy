def add():
    i = 0
    try:
        x = int(input("Veuillez saisir le premier nombre" + "\n"))
        y = int(input("Veuillez saisir le second nombre" + "\n"))
        while type(x) != int or type(y) != int:
            x = int(input("Veuillez saisir le premier nombre" + "\n"))
            y = int(input("Veuillez saisir le second nombre" + "\n"))
            i += 1

    except:
        print("Veuillez saisir des nombres valide")

    else:
        return x + y


def sous():
    try:
        x = int(input("Veuillez saisir le premier nombre" + "\n"))
        y = int(input("Veuillez saisir le second nombre" + "\n"))

    except:
        print("Veuillez saisir des nombres valide")

    else:
        return x - y


def mult():
    try:
        x = int(input("Veuillez saisir le premier nombre" + "\n"))
        y = int(input("Veuillez saisir le second nombre" + "\n"))

    except:
        print("Veuillez saisir des nombres valide")

    else:
        return x * y


def div():
    try:
        x = int(input("Veuillez saisir le premier nombre" + "\n"))
        y = int(input("Veuillez saisir le second nombre" + "\n"))

    except ZeroDivisionError:
        print("Division avec 0 impossible")

    else:
        return x / y


print(add())
