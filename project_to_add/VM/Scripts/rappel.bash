#!/bin/bash

if [[ $# -ge 1 ]]; then
    echo -e "Erreur 1 : Aucun argument n'est attendu."
    exit 1
fi

IFS=$'\n'
for elem in $(cat ../Bdd/emprunts)
do
    nom_adherant=""
    prenom_adherant=""
    titre_livre=""
    auteur_livre=""

    date_partie=$(echo "$elem" | cut -d ";" -f 4)
    jour=$(echo "$date_partie" | cut -d " " -f 1)
    mois=$(echo "$date_partie" | cut -d " " -f 2)
    annee=$(echo "$date_partie" | cut -d " " -f 3)
    hms=$(echo "$date_partie" | cut -d " " -f 4)
    
    categorie_duree_emprunt=$(bash ./comptemps.bash "$jour" "$mois" "$annee" "$hms")
    
    if [[ $categorie_duree_emprunt -eq 1 || $categorie_duree_emprunt -eq 2 ]]; then
        num_adherant=$(echo "$elem" | cut -d ";" -f 1)
        for membres in $(cat ../Bdd/membres)
        do
            if [[ $(echo "$membres" | cut -d ";" -f 1) -eq $num_adherant ]]; then
                nom_adherant=$(echo "$membres" | cut -d ";" -f 2)
                prenom_adherant=$(echo "$membres" | cut -d ";" -f 3)
            fi
        done
        
        num_livre=$(echo "$elem" | cut -d ";" -f 2)
        for livres in $(cat ../Bdd/livres)
        do
            if [[ $(echo "$livres" | cut -d ";" -f 1) -eq $num_livre ]]; then
                titre_livre=$(echo "$livres" | cut -d ";" -f 2)
                auteur_livre=$(echo "$livres" | cut -d ";" -f 3)
            fi
        done

        if [[ -n $nom_adherant ]]; then
            echo "$nom_adherant $prenom_adherant est en retard sur le retour de son exemplaire du titre '$titre_livre' de '$auteur_livre'"
        fi
    fi
done