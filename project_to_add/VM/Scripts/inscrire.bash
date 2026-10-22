#!/bin/bash

IFS=$'\n'

if [[ $1 == "-a" ]]; then
	# AJOUT D'UN ADHERANT DANS membres
	if [[ $# -ne 4 ]]; then
		echo -e "Erreur 1 : Le nombre d'arguments n'est pas correct. \n Usage : $0 -a nom prenom adresse"
		exit 1
	fi
	numero=$(cat ../Bdd/membres | tail -n 1 | cut -d ";" -f 1)
	echo "$((numero+1));$2;$3;$4" >> ../Bdd/membres
	echo "L'adhérant $2 $3 à été ajouté."
elif [[ $1 == "-l" ]]; then

    # CHECK ERREUR
    if [[ $# -ne 3 ]]; then
        echo -e "Erreur 1 : Le nombre d'arguments n'est pas correct. \n Usage : $0 -l titre auteur"
        exit 1
    fi
    
    # AJOUT DANS livres
    dernier_num_livre=$(tail -n 1 ../Bdd/livres 2>/dev/null | cut -d ";" -f 1)
    [[ -z $dernier_num_livre ]] && dernier_num_livre=0
    
    deja_dans_livres=0
    nouveau_num_livre=0

    for livres in $(cat ../Bdd/livres)
    do
        if [[ $(echo "$livres" | cut -d ";" -f 2) == "$2" && $(echo "$livres" | cut -d ";" -f 3) == "$3" ]]; then
            deja_dans_livres=1
            nouveau_num_livre=$(echo "$livres" | cut -d ";" -f 1)
        fi
    done

    if [[ $deja_dans_livres -eq 0 ]]; then
        nouveau_num_livre=$((dernier_num_livre+1))
        echo "$nouveau_num_livre;$2;$3" >> ../Bdd/livres
    else
        echo "Un exemplaire du livre $2 de $3 à été ajouté"
    fi
    
    # AJOUT DANS exemplaire
    exemplaire_max=0
    for ligne_exemplaire in $(cat ../Bdd/exemplaires)
    do
        num_livre_dans_exemplaire=$(echo "$ligne_exemplaire" | cut -d ";" -f 1)
        
        if [[ "$num_livre_dans_exemplaire" -eq "$nouveau_num_livre" ]]; then
            num_exemplaire=$(echo "$ligne_exemplaire" | cut -d ";" -f 2)
            
            if [[ $num_exemplaire -gt $exemplaire_max ]]; then
                exemplaire_max=$num_exemplaire
            fi
        fi
    done

    # On ajoute l'exemplaire suivant (max + 1)
    echo "$nouveau_num_livre;$((exemplaire_max+1));oui" >> ../Bdd/exemplaires
    echo "Le livre $2 à été ajouté."
else
    echo -e "Usage : $0 -a (ajouter un adhérant) / -l (ajouter un livre) \n -a : nom prenom adresse \n -l : titre auteur"
fi