# Korzystając z list oraz słowników stwórz konstrukcja, które będą przechowywać następujące dane.Niech ostatnia kolumna będzie listą.

people = [
    {'id': 1, 'job_title': 'junior developer', 'name': 'John', 'programming_language': ['python']},
    {'id': 2, 'job_title': 'senior dveloper', 'name': 'Mark', 'programming_language': ['python', 'php']},
    {'id': 3, 'job_title': 'stuff dveloper', 'name': 'Alex', 'programming_language': ['php', 'javascript', 'python']},
    {'id': 4, 'job_title': 'junior dveloper', 'name':'Bart', 'programming_language': ['javascript', 'php']},
    {'id': 5, 'job_title': 'senior dveloper', 'name':'Carl', 'programming_language': ['python', 'javascript']},
    {'id': 6, 'job_title': 'junior dveloper', 'name': 'Martha', 'programming_language': ['php', 'javascript']}
]

# Przejdz po liscie i stworz nastepujaca strukture pokazujaca osoby pracujace w danych technologiach

statistics = {}

for worker in people:
    print(worker['name'])
    for programming_language in worker['programming_language']:
        if programming_language not in statistics:
            statistics[programming_language] = {'quantity':0, 'names': []}


        statistics[programming_language]['quantity'] += 1
        statistics[programming_language]['names'].append(worker['name'])


print(statistics)