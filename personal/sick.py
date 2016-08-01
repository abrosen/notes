sen = 1       # P(+|D)
miss = 1 - sen  # P(-|D)


spec = 0.99     # P(-|Dc)
fp  = 1 -spec   # P(+|Dc)


D = (272.1/100000)    # P(D)
Dc = 1 - D 

positive = sen*D + fp*Dc

DgivenPositive =  sen * D /positive
DcGivenPositive = fp *Dc /positive


print(positive)
print(DgivenPositive)
print(DcGivenPositive)
