from itertools import permutations
counter = 0
for x in permutations(range(10)):
    if counter ==999999:
        print x
    counter+=1