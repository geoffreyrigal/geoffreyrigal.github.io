#!/bin/bash

# Verification du nombre d'argument
if [[ $# -ne 2 ]]; then
	echo -e "Erreur 1 : Le nombre d'arguments n'est pas correct. \n Usage : $0 nom titre"
	exit 1
fi

# Verification du nom dans la BDD
verif_nom=0
for lignes in $(cat ../Bdd/membres) # Parcours du fichier membres
do
	nom=$(echo "$lignes" | cut -d ";" -f 2) # Recupération du nom de famille
	if [[ "$nom" == "$1" ]]; then # Si le nom est trouvé dans la BDD
		verif_nom=1
		num_adherant=$(echo "$lignes" | cut -d ";" -f 1)
	fi
done

# Verification du titre dans la BDD
verif_titre=0
for lignes in $(cat ../Bdd/livres)
do
	titre=$(echo "$lignes" | cut -d ";" -f 2)
	if [[ "$titre" == "$2" ]]; then
		verif_titre=1
		num_livre=$(echo "$lignes" | cut -d ";" -f 1)
	fi
done

# Verification de l'exemplaire du titre dans la BDD
verif_dispo=0
for lignes in $(cat ../Bdd/exemplaires)
do
	num_exemplaire=$(echo "$lignes" | cut -d ";" -f 1)
	if [[ "$num_exemplaire" == "$num_livre" ]]; then
		disponibilite=$(echo "$lignes" | cut -d ";" -f 3)
		if [[ "$disponibilite" == "oui" ]]; then
			verif_dispo=1
			num_exemplaire_a_ecrire=$(echo "$lignes" | cut -d ";" -f 2)
			break
		fi
	fi
done

# Test vérification des conditions
if [[ $verif_nom -eq 0 ]]; then
	echo "Le nom de l'adhérant est eronné ou n'existe pas dans la base de donnée."
elif [[ $verif_titre -eq 0 ]]; then
	echo "Le nom du titre est eronné ou n'existe pas dans la base de donnée."
elif [[ $verif_dispo -eq 0 ]]; then
	echo "Aucun exemplaire de $2 n'est disponible."
else # Ecriture des differents fichiers
	date=$(date +"%d %m %Y %H:%M:%S")
	echo "$num_adherant;$num_livre;$num_exemplaire_a_ecrire;$date" >> ../Bdd/emprunts
	sed -i "s/$num_livre;$num_exemplaire_a_ecrire;oui/$num_livre;$num_exemplaire_a_ecrire;non/g" ../Bdd/exemplaires # Mise a jour du fichier exemplaires

	echo "l'exemplaire $num_exemplaire_a_ecrire du livre $2 à bien été emprunté par $1"
fi