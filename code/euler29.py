terms = []

for a in xrange(2,101):
    for b in xrange(2,101):
        terms.append(a**b)

terms = set(terms)
print len(terms)