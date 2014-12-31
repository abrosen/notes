LIMIT  = 59049*20  # this is the real problem
digit5s = []


def sumOf5th(n):
    total = 0
    while n >= 10:
        total +=  (n % 10)**5
        n = n/10
    total += n**5
    return total


for x in range(3, LIMIT):
    if  sumOf5th(x) == x:
        digit5s.append(x)

print sumOf5th(32), 3**5 + 2**5
print digit5s
print sum(digit5s)