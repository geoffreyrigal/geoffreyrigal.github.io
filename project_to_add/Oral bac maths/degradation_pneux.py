import matplotlib.pyplot as plt
import math
import os
from matplotlib import pyplot as pp
import numpy as np
import pandas as pd


#chemin = "C:\\Users\\geoff\\Desktop\\Programmes_Python\\degradation.csv"
#element = pd.read_csv(chemin, header=None)


os.system("cls")
liste_entiers = list(range(1, 62))
liste_entiers_max = list(range(1, 63))

gasly_name = "Gasly"
gasly_list = [31.369,23.214,22.751999999999995,22.706000000000003,22.483000000000004,22.399,22.438999999999993,26.944999999999993,45.303,21.370999999999995,21.501999999999995,21.906000000000006,22.007000000000005,21.839,21.955,22.152,22.391000000000005,22.418999999999997,22.230999999999995,22.233000000000004,22.439999999999998,22.296000000000006,22.614000000000004,22.518,22.607,22.757000000000005,22.721000000000004,23.108999999999995,23.551000000000002,27.962999999999994,44.669,21.406999999999996,21.632999999999996,21.706000000000003,23.385999999999996,21.485,21.658,21.667,21.622,23.459000000000003,23.03,23.721000000000004,21.632999999999996,21.908,23.462999999999994,22.873999999999995,22.242000000000004,21.849999999999994,21.980999999999995,21.905,22.176000000000002,22.186999999999998,21.944999999999993,22.248999999999995,22.53,23.799999999999997,22.959000000000003,23.004000000000005,23.448999999999998,24.010000000000005,23.355000000000004,21.811999999999998,23.467]
gasly_relai = []
gasly_stop = []
gasly_relai_temp = []
gasly_courbe = []
gasly = {}
# Soft --> Hard --> Medium

rus_name = "Russell"
rus_list = [26.498000000000005,21.561999999999998,21.135000000000005,21.628,21.474999999999994,21.492000000000004,21.266999999999996,21.375,21.590999999999994,21.596000000000004,21.465999999999994,21.819999999999993,21.867000000000004,21.817999999999998,21.843999999999994,21.766999999999996,21.991,22.208,22.03,22.215000000000003,26.879999999999995,44.938,20.668999999999997,20.974999999999994,20.950999999999993,21.655,20.736000000000004,21.628,21.444000000000003,22.098,21.516999999999996,21.116,20.933999999999997,21.138999999999996,21.209000000000003,20.902,20.855999999999995,20.689999999999998,20.924000000000007,21.156000000000006,21.108999999999995,21.076999999999998,20.801000000000002,21.164,20.927999999999997,21.227000000000004,21.423000000000002,21.391000000000005,21.158,21.491,21.144999999999996,26.242000000000004,42.845,18.589,19.778000000000006,19.570999999999998,19.456999999999994,19.616,19.881,20.093000000000004,20.703000000000003,21.563000000000002,20.092]
rus_stop = []
rus_relai = []
rus_relai_temp = []
rus_courbe = []
rus = {}
# Médium --> Hard --> Médium

pia_name = "Piastri"
pia_list = [25.726,21.311000000000007,20.808000000000007,21.376999999999995,21.269000000000005,21.307000000000002,21.08,21.522999999999996,21.507999999999996,21.586,21.191000000000003,22.11,21.888000000000005,21.653000000000006,21.679000000000002,21.733999999999995,21.912000000000006,21.867000000000004,22.042,21.852999999999994,22.212000000000003,21.869,26.22,43.263999999999996,19.906999999999996,20.576999999999998,20.784999999999997,20.599000000000004,20.313000000000002,20.578000000000003,20.727999999999994,20.839,20.700999999999993,20.959999999999994,20.912999999999997,20.683999999999997,20.587000000000003,20.498999999999995,20.801000000000002,21.001000000000005,20.965999999999994,21.122,21.333,20.843000000000004,20.888000000000005,21.037999999999997,21.485,21.415999999999997,21.308999999999997,20.979,21.203000000000003,20.777,20.698999999999998,20.412999999999997,20.394000000000005,20.439999999999998,20.602000000000004,20.697999999999993,20.287999999999997,20.649,20.982,20.599000000000004,20.799999999999997]
pia_stop = []
pia_relai = []
pia_relai_temp = []
pia_courbe = []
pia = {}
# Médium --> Hard


ham_name = "Hamilton"
ham_list = [27.111000000000004,21.840999999999994,21.221999999999994,21.715000000000003,21.543999999999997,21.569000000000003,21.445999999999998,21.593000000000004,21.510000000000005,21.543999999999997,21.471999999999994,21.756,21.766999999999996,22.08,21.729,22.198999999999998,21.846000000000004,22.019999999999996,21.974000000000004,22.221999999999994,22.275000000000006,21.846000000000004,21.561000000000007,22.345,21.492000000000004,26.346000000000004,26.215000000000003,43.406000000000006,20.593000000000004,20.586,21.736999999999995,21.159999999999997,20.941999999999993,20.964,22.165000000000006,23.058000000000007,20.748000000000005,20.546000000000006,20.677000000000007,20.837000000000003,20.638999999999996,20.433999999999997,20.331000000000003,20.843000000000004,20.581000000000003,20.944000000000003,21.069000000000003,20.921000000000006,21.182000000000002,20.697999999999993,20.775999999999996,21.176000000000002,21.415000000000006,20.840999999999994,21.027,21.296999999999997,21.664,21.561000000000007,20.649,20.629000000000005,20.726,20.644999999999996,20.649]
ham_stop = []
ham_relai = []
ham_relai_temp = []
ham_courbe = []
ham = {}
# Médium --> Hard

################################################################################################################


def calcul_tt (pilote_list, pilote, pilote_stop, pilote_relai, pilote_relai_temp, name, nbr_stop, diff_tour_pilote_max):

    # Données réelles
    for i in range(1, len(pilote_list)):
        pilote[i] = round(pilote_list[i]+60,3)

    # Calcul du temps total de la course
    total_pilote = 0
    for values in pilote.values():
        total_pilote = total_pilote + values
    esperance = round(total_pilote, 3)
    total_pilote = round(total_pilote / 60, 3)

    # Calcul du tour le plus rapide
    tour_rapide = 10000
    for key, values in pilote.items():
        if key == 0: 
            continue
        else:
            if tour_rapide > values:
                tour_rapide = values

    # Calcul moyenne temps
    moyenne = 0
    tours_pris_en_compte = 0
    for tours in pilote.values():
        if tours > 90:
            continue
        else:
            moyenne = moyenne + tours
            tours_pris_en_compte = tours_pris_en_compte + 1
    moyenne = round(moyenne/tours_pris_en_compte, 3)

    # Séparation des relais
    current_relai = []
    for lap, tps in pilote.items():
        if tps > 90 or lap == 62:
            pilote_relai.append(current_relai)
            current_relai = []
            pilote_stop.append(lap)
        else:  
            current_relai.append(tps)

    # Calcul des difference de temps entre les tours
    diff_tour_pilote_max = []
    for tour in pilote.values():
        calcul = tour - tour_rapide
        diff_tour_pilote_max.append(round(calcul,3))
    
    # Pareil mais dans les relais
    diff_courbe_douce = []
    for i in range(len(diff_tour_pilote_max)-1):
        tps_doux = round((diff_tour_pilote_max[i] + diff_tour_pilote_max[i+1])/2,3)
        diff_courbe_douce.append(tps_doux)

    # Calcul de la variance
    variance_pilote = 0
    nbr = 0
    for temps in pilote.values():
        if temps > 90:
            continue
        else:
            nbr = nbr + 1
            variance_pilote = variance_pilote + ((temps - moyenne)**2)
    variance_pilote = round(variance_pilote/nbr, 3)

    # Calcul de l'écart type
    ecart_pilote = round(math.sqrt(variance_pilote),3)

    # Calcul temps de course estimé
    temps_estime = (moyenne*63 + nbr_stop*28)/60
    
    
    # Régression linéaire
    relai_actu = 1
    print(f"============================== Régression Linéaire {name} ===================================")
    for relai in pilote_relai:
        print(f"=================== Relai {relai_actu} ===================")
        x = np.array(list(range(1, len(relai)+1)))
        y = np.array(relai)
        x_mean = np.mean(x)
        y_mean = np.mean(y)
        b = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
        a = y_mean - b * x_mean
        print("a =", a,"b = ", b )

        y_pred = a + b * x
        ss_total = np.sum((y - y_mean) ** 2)
        ss_residual = np.sum((y - y_pred) ** 2)
        r_squared = 1 - (ss_residual / ss_total)
        print(r_squared)
        relai_actu += 1
    print('')

    # Régression Exponentielle
    relai_actu = 1
    print(f"============================== Régression Exponentielle {name} ===================================")
    for relai in pilote_relai:
        print(f"=================== Relai {relai_actu} ===================")
        x = np.array(list(range(1, len(relai) + 1)))
        y = np.array(relai)

        x_mean = np.mean(x)
        ln_y = np.log(y)
        ln_y_mean = np.mean(ln_y)

        b = np.sum((x - x_mean) * (ln_y - ln_y_mean)) / np.sum((x - x_mean) ** 2)
        
        ln_a = ln_y_mean - b * x_mean
        a = np.exp(ln_a)

        print("a =", a,"b = ", b )

        y_pred = a * np.exp(b * x)
        ss_total = np.sum((y - np.mean(y)) ** 2)
        ss_residual = np.sum((y - y_pred) ** 2)
        r_squared = 1 - (ss_residual / ss_total)
        print(r_squared)
        relai_actu += 1
    print("=================================================================\n")
    """
    # Calcul du taux de dégradation des pneux
    comp_tempo = []
    comparaison_usure_def = [1000000, 0, 0]

    for coef in np.arange(0, 0.25, 0.05):
        for coef_exp in np.arange(0, 0.05, 0.001):
            temps = 0
            for tps in pilote.values():
                usure_pneux = round((coef*temps) + (coef_exp*(temps)**2),3)
                comp_tempo.append(usure_pneux)
                temps += round(tps/60,3)

            comparaison_usure_temp = 0
            tour_usure = 0
            for tours in pilote.values():
                rapport = tour_rapide - (tour_rapide*comp_tempo[tour_usure])
                comparaison_usure_temp += rapport
                print(comparaison_usure_temp)
            if comparaison_usure_temp < comparaison_usure_def[0] and comparaison_usure_temp >= 0:
                comparaison_usure_def = [comparaison_usure_temp, coef, coef_exp]
            print(comp_tempo)
            comp_tempo = []
    print(comparaison_usure_def)
    """

    print('Temps estimé de ', name, '=',temps_estime)
    print("Moyenne", name,"=", moyenne)
    print('Esperance de', name, "=", esperance)
    print("Variance", name, "=", variance_pilote)
    print("Ecart type", name, "=", ecart_pilote)
    print("Temps de course total", name, "=", total_pilote)
    print("------------------------------------------------------------")
    print("Temps", name, "=", pilote, "\n")
    print("Difference entre Ti et Tmin",name," : ", diff_tour_pilote_max, "\n\n\n")
    print("########################################################################################################################")
    print("######################################################################################################################## \n")

    pp.plot(liste_entiers, diff_courbe_douce, label=name)
    #pp.plot(liste_entiers_max, pilote.values(), label = name)
    pp.plot(liste_entiers_max, diff_tour_pilote_max, label=name)

#calcul_tt(gasly_list, gasly, gasly_stop, gasly_relai, gasly_relai_temp, gasly_name, 2, gasly_courbe)
calcul_tt(rus_list, rus, rus_stop, rus_relai, rus_relai_temp, rus_name, 2, rus_courbe)
#calcul_tt(pia_list, pia, pia_stop, pia_relai, pia_relai_temp, pia_name, 1, pia_courbe)
calcul_tt(ham_list, ham, ham_stop, ham_relai, ham_relai_temp, ham_name, 1, ham_courbe)

pp.ylim(0,5)
pp.legend()
pp.show()

# chronof1.com
# Grand prix Imola 2024
# Temps dans les stands = 28s

# A faire : 
# Nbr d'arret au stand pour les gagnants
# Loi des probas : p = nombre d'arret, p(X = xi) = Occurence de victoire
# Loi des probas : p = nombre d'arret, p(X = xi) = Temps de la course
# Expliquer 