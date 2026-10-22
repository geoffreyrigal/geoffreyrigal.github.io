import requests

tbl1 = {"1": 0, "2": 0, "3": 0,}
tbl2 = {"num_course":["nbr arret", "temps"],}

def get_number_of_races(year):
    if year == 2024:
        return 10
    else:
        url = f"http://ergast.com/api/f1/{year}.json"
        response = requests.get(url)
        data = response.json()

        number_of_races = len(data['MRData']['RaceTable']['Races'])

        return number_of_races

def get_infos(year, round):
    url = f"http://ergast.com/api/f1/{year}/{round}/results/1.json"
    response = requests.get(url)
    data = response.json()

    winner = data['MRData']['RaceTable']['Races'][0]['Results'][0]['Driver']['driverId']
    time = data['MRData']['RaceTable']['Races'][0]['Results'][0]['Time']['time']
    race = data['MRData']['RaceTable']['Races'][0]['raceName']
    return winner, time, race

def get_pit_stops(year, round, driver):
    url = f"http://ergast.com/api/f1/{year}/{round}/drivers/{driver}/pitstops.json"
    response = requests.get(url)
    data = response.json()

    races = data['MRData']['RaceTable']['Races']
    if races and 'PitStops' in races[0]:
        pit_stops = races[0]['PitStops']
        return len(pit_stops)
    else:
        return 0 

num_course = 0
for annee in range (2021,2022):
    print(annee)
    for course in range (1,get_number_of_races(annee)+1):

        gagnant, temps, nom_course = get_infos(annee, course)
        nbr_pitstop = get_pit_stops(annee, course, gagnant.lower())

        if nbr_pitstop <= 3 and nbr_pitstop != 0:
            tbl1[str(nbr_pitstop)] += 1
            tbl2[num_course] = [str(nbr_pitstop),temps]
            num_course += 1

print(tbl1)
print(tbl2)