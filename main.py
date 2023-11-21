""" Auteur : Maxime Malpica Arana
    Matricle : HE202259
    Date de création : lundi 13 novembre 2023 à 09:48
    Dernière mise a jour : jeudi 16 novembre 2023 à 11:30
    Description du code : Script qui tri des fichiers via leur extensions utilisable en ligne de commande """

#------------------------------Librairie nécessaire pour le script------------------------------#
import argparse
import os
import time
from tkinter import *
from tkinter import filedialog
from tkinter import Label

#------------------------------Fonction qui génere l'ig------------------------------#
def interface_graphique():
    window = Tk()
    window.title("Liste des fichiers")
    window.geometry('200x400')
    dossier_selectionner_ig = ""
    dernier_dossier_selectionner_ig = ""

    #------------------------------Fonction utilitaire qui affiche les données du tableau reçu en paramètre sous forme de colonne------------------------------#
    def affichage_colonne(tableau):
        for ind,val in enumerate(tableau):
            label = Label(window, text=val)
            label.grid(column=0,row=ind+3)
    
    #------------------------------Fonction utilitaire qui supprime les données du tableau reçu en paramètre sous forme de colonne------------------------------#
    def clear_colonne(tableau):
        for ind,val in enumerate(tableau):
            for data in window.grid_slaves(column=0, row=ind+3):
                data.destroy()
    
    #------------------------------Fonction principale du bouton "Rechercher un dossier 👀" qui permet de récupérer et d'afficher un dossier------------------------------#
    def affichage_dossier_choisi_ig():
        global dossier_selectionner_ig
        global dernier_dossier_selectionner_ig
        dossier_selectionner_ig = filedialog.askdirectory()
        try:
            if dernier_dossier_selectionner_ig:
                tableau_de_fichier = recuperation_fichier(dossier_selectionner_ig)
                tableau_de_fichier_a = recuperation_fichier(dernier_dossier_selectionner_ig)
                clear_colonne(tableau_de_fichier_a)
                affichage_colonne(tableau_de_fichier)
                dernier_dossier_selectionner_ig = dossier_selectionner_ig
        except NameError:
            tableau_de_fichier = recuperation_fichier(dossier_selectionner_ig)
            dernier_dossier_selectionner_ig = dossier_selectionner_ig
            affichage_colonne(tableau_de_fichier)

    #------------------------------Fonction principale du bouton "Tri croissant" qui trie dans l'ordre croissant le dossier choisi------------------------------#
    def tri_croissant():
        global dossier_selectionner_ig
        tableau_du_fichier_a_trier_croi_ig = recuperation_fichier(dossier_selectionner_ig)
        tableau_fichier_trier_croissant_ig = tri_de_dossier("croissant", tableau_du_fichier_a_trier_croi_ig)
        clear_colonne(tableau_du_fichier_a_trier_croi_ig)
        affichage_colonne(tableau_fichier_trier_croissant_ig)

    #------------------------------Fonction principale du bouton "Tri décroissant" qui trie dans l'ordre décroissant le dossier choisi------------------------------#
    def tri_decroissant():
        global dossier_selectionner_ig
        tableau_fichier_a_trier_decroi_ig = recuperation_fichier(dossier_selectionner_ig)
        tableau_fichier_trier_decroissant_ig = tri_de_dossier("décroissant", tableau_fichier_a_trier_decroi_ig)
        clear_colonne(tableau_fichier_a_trier_decroi_ig)
        affichage_colonne(tableau_fichier_trier_decroissant_ig) 

    bouton_choix_dossier_ig = Button(window, text="Rechercher un dossier 👀", command=affichage_dossier_choisi_ig)
    bouton_choix_dossier_ig.grid(column=0, row=0) 
    bouton_choix_croiss_ig = Button(window, text="Tri croissant", command=tri_croissant)
    bouton_choix_croiss_ig.grid(column=0, row=1)
    bouton_choix_decroiss_ig = Button(window, text="Tri décroissant", command=tri_decroissant)
    bouton_choix_decroiss_ig.grid(column=0, row=2)
    window.mainloop()

    
#------------------------------Fonction utilitaire qui renvoie sour forme de tableau tout les fichiers avec extension d'un dossier grâce au chemin de celui-ci en paramètre------------------------------#
def recuperation_fichier(chemin):
    contenu_dossier = os.listdir(f"{chemin}")
    nouveau_tableau = []
    for i in contenu_dossier:
        dd = os.path.join(chemin,i)
        if os.path.isfile(dd):
            nom_fichier, extension = os.path.splitext(i)
            
            if extension :
                nouveau_tableau.append(i)
    return nouveau_tableau


#------------------------------Fonction utilitaire qui renvoie un tableau trié en fonction du type de tri défini en paramètre------------------------------#
def tri_de_dossier(typeDeTri, tableauATrier):
    if typeDeTri == "croissant":
        tableau_croissant = sorted(tableauATrier, key=lambda x: x[-3:].lower(), reverse=False)
        return tableau_croissant
    if typeDeTri == "décroissant":
        tableau_decroissant = sorted(tableauATrier, key=lambda x: x[-3:].lower(), reverse=True)
        return tableau_decroissant

#------------------------------Debut du script#------------------------------#
parser = argparse.ArgumentParser()
parser.add_argument("-I","--interfaceGraphique", choices=['oui', 'non'], help="défini si il faut un interface graphique")
args = parser.parse_args()
choix_inteface_graphique = args.interfaceGraphique
time.sleep(1)

#------------------------------Condition qui traîte la présence d'un ig------------------------------#
if choix_inteface_graphique == "oui":
    print("Lancement du script avec interface graphique.")
    time.sleep(2)
    interface_graphique()
elif choix_inteface_graphique == "non":
    print("Lancement du script sans interface graphique.")
    time.sleep(1)
    choix_dossier_noig = input("Entrez le chemin relatif vers votre dossier a trié : ")
    tableau_du_dossier_noig = recuperation_fichier(choix_dossier_noig)
    aff_dossier_hor_noig = " / ".join(tableau_du_dossier_noig)
    print(aff_dossier_hor_noig)
    time.sleep(1)
    choix_tri_noig= input("Entrez le type de tri (croissant, décroissant): ")
    while choix_tri_noig.lower() not in ['croissant', 'décroissant']:
        print("Erreur : Veuillez entrer 'croissant' ou 'décroissant'.")
        choix_tri_noig = input("Entrez le type de tri (croissant, décroissant) : ")
    tableau_du_dossier_trie_noig = tri_de_dossier(choix_tri_noig, tableau_du_dossier_noig)
    aff_dossier_trie_hor_noig = " / ".join(tableau_du_dossier_trie_noig)
    print(aff_dossier_trie_hor_noig)
