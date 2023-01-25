import random
myster = random.randint(1, 100)

saisi = int(input("Essayer de deviner le nombre" + "\n"))
print(saisi)
#print(f"le nombre à deviner est {myster}")
i = 0
while i < 2 and myster != saisi:
    saisi = int(input("Réessayer de deviner le nombre" + "\n"))
    print(saisi)
    i += 1
    if myster > saisi:
        print("Le nombre à deviner est plus grand")
    elif myster < saisi:
        print("Le nombre à deviner est plus petit")

    else:
        print("Vous avez deviner le nombre")
        exit()

    if i == 2:
        print("Vous avez perdu")
        print(f"le nombre à deviner était {myster}")

