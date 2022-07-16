from random import *

def affichage(grille):
    for ligne in grille:
        ligne_affichee=""
        for elt in ligne:
            if elt==0:
                ligne_affichee+="[   ]"
            if elt==1:
                ligne_affichee+="[ X ]"
            if elt==2:
                ligne_affichee+="[ O ]"
        print(ligne_affichee)

grille=[[0]*7 for _ in range(6)]
print(affichage(grille))



def jouer_un_jeton(grille, num_joueur, colonne):
    assert colonne <=6 , "Les colonnes sont numérotées de 0 à 6"
    jetonj1=1
    jetonj2=2
    if grille[0][colonne] != 0 :
        return False
    else:
        for elt in range(5,-1,-1):
            if grille[elt][colonne]==0 and num_joueur==1:
                grille[elt][colonne]=jetonj1
                return True and affichage(grille)

            elif grille[elt][colonne]==0 and num_joueur==2:
                grille[elt][colonne]= jetonj2
                return True and affichage(grille)

def play_a_game(grille):
    game = 'y'
    compteur = 0
    while game == 'y' :
        game = input('Voulez-vous continuer ?')
        compteur += 1
        if game == 'y':
            player = int(input('Quel joueur veut jouer ?'))
            colone = int(input('quelle colone voulez-vous jouer ?'))
            print(jouer_un_jeton(grille,player,colone))
        else :
            return('Game terminer !', compteur-1)
        
print(play_a_game(grille))
