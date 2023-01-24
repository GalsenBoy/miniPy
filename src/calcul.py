def add():
    try:
        x = int(input("Veuillez saisir le premier nombre" + "\n"))
        y = int(input("Veuillez saisir le second nombre" + "\n"))

    except ValueError:
        print("Veuillez saisir des nombres valide")

    else:
        return x + y


def sous():
    try:
        x = int(input("Veuillez saisir le premier nombre" + "\n"))
        y = int(input("Veuillez saisir le second nombre" + "\n"))

    except ValueError:
        print("Veuillez saisir des nombres valide")

    else:
        return x - y


def mult():
    try:
        x = int(input("Veuillez saisir le premier nombre" + "\n"))
        y = int(input("Veuillez saisir le second nombre" + "\n"))

    except ValueError:
        print("Veuillez saisir des nombres valide")

    else:
        return x * y


def div():
    try:
        x = int(input("Veuillez saisir le premier nombre" + "\n"))
        y = int(input("Veuillez saisir le second nombre" + "\n"))
        assert y != 0

    except AssertionError:
        print("Division avec 0 impossible")

    except ValueError:
        print("Veuillez saisir des nombres valide")

    else:
        return x / y


print(div())
