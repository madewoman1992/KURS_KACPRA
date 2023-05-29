# Stwórz słownik zawierający informacje o swoich ulubionych filmach (tytuł, reżyser, rok produkcji).
# Następnie usuń ze słownika filmy, których reżyserem jest Steven Spielberg.

filmy = {'tytul': 'Gladiator', 'rezyser': 'RS', 'rok produkcji': '2019', 'tytul': 'XYZ', 'rezyser': 'Spielberg', 'rok produkcji': '2000', 'tytul': 'MUR', 'rezyser': 'Coco', 'rok produkcji': '3401', 'tytul': 'ffff', 'rezyser': 'Spielberg', 'rok produkcji': '2019'}

for i in filmy:
    if filmy.values() == 'Spielberg':
        del filmy['Spielberg']

print(filmy)

