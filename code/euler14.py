def generateCollatz(limit):
    colSeq =  {}
    colSeq[1] = 1
    for node  in range(2,limit):
        steps = 1
        i = node  
        while i >=node:
            if i % 2 == 0:
                i = i/2
            else:
                i = 3*i +1
            if i in colSeq:
                break
            steps += 1
        colSeq[node] =  steps + colSeq[i]
    return colSeq



def main():
    seq = generateCollatz(1000000)
    print max(seq, key=seq.get)

if __name__ == '__main__':
    main()