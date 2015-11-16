def isAnagram(s1,s2):
    h1 = {}
    h2 = {}
    for c in s1:
        if c in h1.keys():
            h1[c] = h1[c] +1
        else:
            h1[c] = 1
    for c in s2:
        if c in h2.keys():
            h2[c] = h2[c] +1
        else:
            h2[c] = 1
    if h1 == h2:
        return True
    return False

print(isAnagram("bat", "tab"))
print(isAnagram("heart", "gold"))

