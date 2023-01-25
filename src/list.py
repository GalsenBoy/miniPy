basket = []

print("1: Rajouter un produit dans votre panier" + "\n" +
      "2: Supprimer un produit de votre liste" + "\n" +
      "3: Voir la liste de votre panier" + "\n" +
      "4: Vider votre panier" + "\n" +
      "5: Sortir de l'application")

choice = 0

while choice > 1 or choice <= 5:
    choice = int(input("Que voulez-vous faire" + "\n"))
    if choice == 1:
        add = input("Veuillez entrer le produit à ajouter")
        basket.append(add)
        print(f"Votre produit {add} a été ajouté avec succès dans votre panier")
    elif choice == 2:
        delete = input("Veuillez saisir le produit à supprimer")
        if delete in basket:
            basket.remove(delete)
            print(f"Le produit {delete} a été supprimé avec succès dans votre panier")
        else:
            print("Le produit n'existe pas dans votre panier")

    elif choice == 3:
        for index, value in enumerate(basket, 1):
            print(index, value)

    elif choice == 4:
        basket.clear()

    else:
        exit()




