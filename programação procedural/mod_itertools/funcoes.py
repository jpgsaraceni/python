"""
count - contador
zip_longest - junta dois iteráveis usando todos os valores.
    ]pode estabelecer valor padrão para se não forem fornecidos todos os valores usando fillvalue=
combinations - faz combinações (ordem n importa)
permutations - ordem importa
product - repete >> product(<lista>, repeat=<n>)
"""
from itertools import combinations

pessoas = ['a', 'b', 'c', 'd']

for comb in combinations(pessoas, 2):
    print(comb)