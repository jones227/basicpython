import random

spør = int(input('hvor mange skal trekkes? '))

navn = ['Johannes', 'Kevin', 'Deimantas', 'Haidas', 'Marius', 'Benjamin', 'Benedict', 'Romandus', 'Robin', 'Markus',
        'Eirik', 'william']


def trekk_tilfeldig(n):
    trekk = random.sample(navn, n)
    return trekk


print(*trekk_tilfeldig(spør), sep="\n")
