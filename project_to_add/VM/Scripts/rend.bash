#!/bin/bash

# Verification du nombre d'argument
if [[ $# -ne 2 ]]; then
	echo -e "Erreur 1 : Le nombre d'arguments n'est pas correct. \n Usage : $0 nom titre"
	exit 1
fi

# Verification du nom dans la BDD
verif_nom=0
for lignes in $(cat ../Bdd/membres)
do
	nom=$(echo "$lignes" | cut -d ";" -f 2)
	if [[ "$nom" == "$1" ]]; then
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

if [[ $verif_nom -eq 0 ]]; then
	echo "'$1' n'as pas été trouvé dans la base de donnée."
elif [[ $verif_titre -eq 0 ]]; then
	echo "'$2' n'as pas été trouvé dans la base de donnée."
else
	# Verifie si l'emprunt existe et supprimer/momdifie les données dans les fichiers correspondants
	verif_emprunt=0
	compteur=0
	for lignes in $(cat ../Bdd/emprunts | cut -d ";" -f 1-3)
	do
		((compteur++))
		id_membre_emprunt=$(echo "$lignes" | cut -d ";" -f 1)
		id_livre_emprunt=$(echo "$lignes" | cut -d ";" -f 2)
		id_exemplaire_emprunt=$(echo "$lignes" | cut -d ";" -f 3)
		if [[ $id_membre_emprunt == $num_adherant && $id_livre_emprunt == $num_livre ]]; then
			verif_emprunt=1
			sed -i "${compteur}d" ../Bdd/emprunts
			for ex in $(cat ../Bdd/exemplaires)
			do
				if [[ $(echo "$ex" | cut -d ";" -f 1) -eq $id_livre_emprunt && $(echo "$ex" | cut -d ";" -f 2) -eq $id_exemplaire_emprunt ]]; then
					sed -i "s/$num_livre;$id_exemplaire_emprunt;non/$num_livre;$id_exemplaire_emprunt;oui/g" ../Bdd/exemplaires
				fi
			done
			break
		fi
	done

	if [[ verif_emprunt -eq 0 ]]; then
		echo "Aucun emprunt de l'adhérant '$1' sur le titre '$2' n'a été effectué."
	else
		echo "L'adhérant '$1' à bien rendu '$2'."
	fi
fi