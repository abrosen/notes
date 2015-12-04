def allUnique(string):
    t = {}
    for c in string:
        if c in t:
            return False
        else:
            t[c] = 1
    return True
    
def allUniqueNoCheat(string):
    for i in range(0,len(string)):
        for j in range(i+1, len(string)):
            if c[i] == c[j]:
                return False
    return True

print(allUnique("Foo"))
print(allUnique("Bar"))
print(allUnique("the lazy man"))
