#!/bin/bash

# Verification du nombre d'arguments
if [[ $# -ne 4 ]]; then
    echo -e "Erreur 1 : Le nombre d'arguments n'est pas correct. \n Usage : $0 jour mois année heure:minute:secondes"
    exit 1
fi

# Vérification des valeurs des arguments
if [[ $1 -lt 1 || $1 -gt 31 ]]; then
    echo -e "Erreur 2 : La valeur du jour n'est pas correcte. \n Doit être comprise entre 1 et 31"
    exit 2
elif [[ $2 -lt 1 || $2 -gt 12 ]]; then
    echo -e "Erreur 3 : La valeur du mois n'est pas correcte. \n Doit être comprise entre 1 et 12"
    exit 3
else
    # Gestion des dates
    date_brute=$(date +"%-d %-m %Y")
    date_actu=($date_brute) 
    date_args=($1 $2 $3)

    # Nombre de jours dans une année
    mois=(31 28 31 30 31 30 31 31 30 31 30 31)

    retenue_mois=0
    retenue_annee=0

    # Calcul jours
    diff_jour=$(( date_actu[0] - date_args[0] ))

    if [[ $diff_jour -lt 0 ]]; then
        index_mois_prec=$(( date_actu[1] - 2 ))
        [[ $index_mois_prec -lt 0 ]] && index_mois_prec=11
        
        diff_jour=$(( diff_jour + ${mois[$index_mois_prec]} ))
        retenue_mois=1
    fi

    # Calcul mois
    diff_mois=$(( date_actu[1] - date_args[1] - retenue_mois ))

    if [[ $diff_mois -lt 0 ]]; then
        diff_mois=$(( diff_mois + 12 ))
        retenue_annee=1
    fi

    # Calcul années
    diff_annee=$(( date_actu[2] - date_args[2] - retenue_annee ))

    # Cas 0 : Date argument est postérieure ou égale à la date courante
    if [[ $diff_annee -lt 0 ]] || [[ $diff_annee -eq 0 && $diff_mois -lt 0 ]] || [[ $diff_annee -eq 0 && $diff_mois -eq 0 && $diff_jour -le 0 ]]; then
        echo 0
    # Cas 1 : Antérieure de plus d'un an
    elif [[ $diff_annee -ge 1 ]]; then
        echo 1
    # Cas 2 : Antérieure de plus d'un mois et moins d'un an
    elif [[ $diff_mois -ge 1 ]]; then
        echo 2
    # Cas 3 : Antérieure de moins d'un mois
    else
        echo 3
    fi
fi