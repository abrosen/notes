import math
C = [x **2 for x in range(1,2000)]
print C

for i in range(0,len(C)):
    for j in range(i, len(C)):
        for k in range(j, len(C)):
            x = C[i]+C[j]+C[k]
            if C[i] + C[j] == C[k] and int(math.sqrt(C[i]) +math.sqrt(C[j])+ math.sqrt(C[k])) ==1000: 
                print math.sqrt(C[i]),math.sqrt(C[j]),math.sqrt(C[k]),   math.sqrt(x)
                print math.sqrt(C[i])*math.sqrt(C[j])*math.sqrt(C[k])
                

