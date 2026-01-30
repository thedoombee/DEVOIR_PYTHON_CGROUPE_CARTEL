# Mise en place d'un algorithme qui suit la logique d'une application de gestion de stocks en verifiant tous les concepts 

# Initialisation de la liste des produits
stocks = []

def ajouter_produit(nom, qte):
    """Ajoute un produit au stock"""
    if qte > 0:
        produit = {"nom": nom, "qte": qte}
        stocks.append(produit)
        print(f"Produit '{nom}' ajouté avec {qte} unités")
    else:
        print("Erreur: la quantité doit être positive")

def supprimer_produit(nom):
    global stocks
    stocks = [p for p in stocks if p["nom"] != nom]
    print(f"Produit '{nom}' supprimé")

def mettre_a_jour_qte(nom, nouvelle_qte):
    """Met à jour la quantité d'un produit"""
    for produit in stocks:
        if produit["nom"] == nom:
            produit["qte"] = nouvelle_qte
            print(f"Quantité de '{nom}' mise à jour: {nouvelle_qte}")
            return
    print(f"Produit '{nom}' non trouvé")

def afficher_stocks():
    """Affiche tous les produits en stock"""
    print("\n--- STOCK ACTUEL ---")
    for produit in stocks:
        print(f"{produit['nom']}: {produit['qte']} unités")
    print("-------------------\n")

def rechercher_produit(nom):
    """Recherche un produit par son nom"""
    for produit in stocks:
        if produit["nom"] == nom:
            return produit
    return None

def acheter_produit(nom, qte):
    """Réduit la quantité d'un produit lors d'un achat"""
    for produit in stocks:
        if produit["nom"] == nom:
            if produit["qte"] >= qte:
                produit["qte"] -= qte
                print(f"Achat de {qte} unités de '{nom}' effectué. Stock restant: {produit['qte']}")
                return
            else:
                print(f"Erreur: stock insuffisant. Disponible: {produit['qte']}")
                return
    print(f"Produit '{nom}' non trouvé")

def demarage():
    
    print("GESTION DE STOCK")
    
    while True:
        print("\n1. Ajouter un produit")
        print("2. Afficher les stocks")
        print("3. Mettre à jour une quantité")
        print("4. Rechercher un produit")
        print("5. Supprimer un produit")
        print("6. Acheter un produit")
        print("7. Quitter")
        
        choix = input("Choisissez une option: ")
        
        if choix == "1":
            nom = input("Nom du produit: ")
            qte = int(input("Quantité: "))
            ajouter_produit(nom, qte)
        elif choix == "2":
            afficher_stocks()
        elif choix == "3":
            nom = input("Nom du produit: ")
            qte = int(input("Nouvelle quantité: "))
            mettre_a_jour_qte(nom, qte)
        elif choix == "4":
            nom = input("Nom du produit: ")
            produit = rechercher_produit(nom)
            print(produit if produit else "Produit non trouvé")
        elif choix == "5":
            nom = input("Nom du produit: ")
            supprimer_produit(nom)
        elif choix == "6":
            nom = input("Nom du produit: ")
            qte = int(input("Quantité à acheter: "))
            acheter_produit(nom, qte)
        elif choix == "7":
            print("Au revoir!")
            break

demarage()
