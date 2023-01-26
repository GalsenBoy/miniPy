import json

basket = "C:/Users/Cissokho/Documents/data.json"


def print_choice():
    print("1: Rajouter un produit dans votre panier \n" +
          "2: Supprimer un produit de votre liste \n" +
          "3: Voir la liste de votre panier \n" +
          "4: Vider votre panier \n" +
          "5: Sortir de l'application")


print_choice()

choice = 0
while choice > 1 or choice <= 5:
    choice = int(input("Que voulez-vous faire \n"))
    if choice == 1:
        add = input("Veuillez entrer le produit à ajouter \n")
        with open(basket, "r", encoding="utf-8") as file:
            data = json.load(file)
            data.append(add)
        with open(basket, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Votre produit {add} a été ajouté avec succès dans votre panier \n")
    elif choice == 2:
        delete = input("Veuillez saisir le produit à supprimer \n")
        with open(basket, "r", encoding="utf-8") as file:
            data = json.load(file)
            if delete in data:
                data.remove(delete)
                print(f"Le produit {delete} a été supprimé avec succès dans votre panier \n")
            else:
                print("Le produit n'existe pas dans votre panier \n")

        with open(basket, "w", encoding="utf-8") as file:
            json.dump(data, file)

    elif choice == 3:
        with open(basket, "r", encoding="utf-8") as file:
            data = json.load(file)
            if data:
                for index, value in enumerate(data, 1):
                    print(index, value)
            else:
                print("Votre liste est vide \n")

    elif choice == 4:
        with open(basket, "r", encoding="utf-8") as file:
            data = json.load(file)
            data.clear()
        with open(basket, "w") as file:
            json.dump(data, file)

        print("Votre liste a été vidé avec succès \n")
    else:
        print("A bientôt")
        exit()
    print_choice()
