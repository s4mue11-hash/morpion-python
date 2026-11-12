import sys


def creer_grille():
    grille = [[" "," "," "],[" "," "," "],[" "," "," "]]
    #print(len(grille))
    #print(len(grille[0]))
    return grille

def afficher_grille(grille):
    for ligne in grille:
        
        for case in ligne:
            print(case, end = "|")
        print()
        print("-------")

def verifier_victoire(grille,joueur):
    
    cv=0
    cd1=0
    cd2=0
    for indice_ligne in range(len(grille)) :     
            ch=0 
            cv=0
            for indice_colonne in range (len(grille[indice_ligne])):
                if grille[indice_ligne][indice_colonne]==joueur:
                    ch+=1
                if grille[indice_colonne][indice_ligne]==joueur:
                    cv+=1
        
            if ch==3:
                return True
            if cv == 3:
                return True
    for indice_ligne in range(len(grille)):
        if grille[indice_ligne][indice_ligne]==joueur:
            cd1+=1
    if cd1==3:
        return True
    for indice_ligne in range((len(grille))):
        indice_colonne=len(grille)-1-indice_ligne
        if grille[indice_ligne][indice_colonne]==joueur:
            cd2+=1
            
            
    if cd2==3:
        return True



    return False

def grille_complete(grille):
    for indice_ligne in range(len(grille)):
        for  indice_colonne in range(len(grille[indice_ligne])):
            if grille[indice_ligne][indice_colonne]==" ":
                return False
    return True



    

            

def jouer_coup(grille,joueur):

    while True:

        try:
            ligne = int(input("numéro de la ligne : "))
            if ligne<1 or ligne>3:
                raise ValueError("choisissez des coordonnées entre 1 et 3")
            ligne-=1
            colonne = int(input("numéro de colonne : "))
            if colonne<1 or colonne>3:
                raise ValueError("choisissez des coordonnées entre 1 et 3")
            colonne-=1
            if grille[ligne][colonne]!= " ":
                print("La case n'est pas libre !!!\nDonne une nouvelle position")
                #ligne = int(input("numéro de la ligne : "))
                
                #colonne = int(input("numéro de colonne : "))
            else:
                grille[ligne][colonne] = joueur
                break

            afficher_grille(grille)
        except ValueError as e :
            print(f"{e}")
            continue

def jouer():
    grille=creer_grille()
    print("Bienvenu dans le morpion : jouez 'X' et 'O' !\n")
    while True:

        joueur="X"
        afficher_grille(grille)
        jouer_coup(grille,joueur)
        verifier_victoire(grille,joueur)
        if verifier_victoire(grille,joueur)==True:
            print("le joueur X a gagné!!!!")
            afficher_grille(grille)
            break
        grille_complete(grille)
        if grille_complete==True:
            print("il y'a égalité !!!")
            afficher_grille(grille)
            break
        afficher_grille(grille)
        joueur = "O"
        jouer_coup(grille,joueur)
        verifier_victoire(grille,joueur)
        if verifier_victoire(grille,joueur) == True:
            print("le joueur O a gagné !!!!")
            afficher_grille(grille)
            break 
        grille_complete(grille)
        if grille_complete(grille)==True:
            print("il y'a egalité !!!")
            afficher_grille(grille)
            break 

        







    
#main
#print(creer_grille())
#grille = creer_grille()
#afficher_grille(grille)
#jouer_coup(grille,"X")
#print(verifier_victoire(grille,"X"))
jouer()

