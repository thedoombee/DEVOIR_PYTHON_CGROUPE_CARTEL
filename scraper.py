import requests
from bs4 import BeautifulSoup

response = requests.get("http://127.0.0.1:5500/")
soup = BeautifulSoup(response.text, "html.parser")

if response.status_code == 200:
    # Récupération de toutes les  images sur le site 
    print("-------------------------------------------------------------------------------")
    print("Affichage des images ")
    print("-------------------------------------------------------------------------------")
    images = soup.find_all("img")
    # Affichage des images par la boucle for
    for image in images:
        print(image)

    # Récupération des titres 
    print("-------------------------------------------------------------------------------")
    print("Affichage des titres ")
    print("-------------------------------------------------------------------------------")
    grandstitres = soup.find_all("h1")
    titres = soup.find_all("h2")
    soustitres = soup.find_all("h3")
    
    for grandstitre in grandstitres:
        print(grandstitre.text)

    for titre in titres:
        print(titre.text)
    
    for soustitre in soustitres:
        print(soustitre.text)

    

    # Recuperations de tous les paragraphes

    paragraphes = soup.find_all("p")
    print("-------------------------------------------------------------------------------")
    print("Voici tous les paragraphes")
    print("-------------------------------------------------------------------------------")
    for paragraphe in paragraphes:
        print(paragraphe.text)

    # Recuperation du formulaire 

    formulaire = soup.find("form")
    print("-------------------------------------------------------------------------------")
    print("Affichage du formulaire ")
    print("-------------------------------------------------------------------------------")
    print(formulaire)

    # Recuperation des liens
    print("-------------------------------------------------------------------------------")
    print("Affichages des liens")
    print("-------------------------------------------------------------------------------")
    liens = soup.find_all("a")

    for lien in liens:
        print(lien.get("href"))
else:
    print("Erreur lors de la connexion au site ")