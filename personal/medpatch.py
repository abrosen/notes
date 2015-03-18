## Program for extremely rough estimate of mythyl based on halflife of 2-4 hours
## I am not a doctor, this is for my own personal use.
## I am not liable for any use of this program by anyone else
## see relvenent terms of the GNU 3



#could model like a nicotine patch

import numpy as np
import matplotlib.pyplot as plt


def decay(initial, t, halflife):
    return initial * (.5)**(t/halflife)


def getLevels(initial, supplemental, halflife, interval,  num_sup=2, max_time=24):
    times = np.arange(0,max_time,0.1)
    levels = [decay(initial, t, halflife) for t in times]
    for offset in xrange(1,num_sup+1):
        sup_levels =  np.zeros(interval*offset/0.1)
        sup_levels =  list(sup_levels) + [decay(supplemental, t - interval*offset, halflife) for t in np.arange(interval*offset,max_time,0.1)]
        print sup_levels
        for i in xrange(len(levels)):
            levels[i] = levels[i]+sup_levels[i]


    return times, levels

times0, levels0 =  getLevels(10,10,2.1,3.5)
times1, levels1 =  getLevels(10,10,2.5,3.5)
times2, levels2 =  getLevels(10,10,2.9,3.5)
times3, levels3 =  getLevels(10,10,3.3,3.5)

plt.plot(times0,levels0, 'go-',label = "half-life = 2.1")
plt.plot(times1,levels1, 'ko-',label = "half-life = 2.5")
plt.plot(times2,levels2, 'ro-',label = "half-life = 2.9")
plt.plot(times3,levels3, 'bo-',label = "half-life = 3.3")


plt.xlabel("Hours")
plt.ylabel("mg")
plt.grid()
plt.legend()
plt.show()