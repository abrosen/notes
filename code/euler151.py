import random
NUM_TRIALS = 100000


def getA5(envelope):
    """Takes a single piece from the envolope and cuts it until we get to an A5.  Unused pieces return to the envolope."""
    pick = random.choice(envelope)
    envelope.remove(pick)
    while pick < 5:
        pick +=1
        envelope.append(pick)
    #return pick 

def main():
    totalSingles = 0
    for i in xrange(NUM_TRIALS):
        envelope = [2,3,4,5]
        singles = 0  
        for j in xrange(14):
            if len(envelope) == 1:
                singles += 1 
            getA5(envelope)
        totalSingles +=  singles
    print float(totalSingles)/NUM_TRIALS



if __name__ == '__main__':
    main()