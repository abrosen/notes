## Program for extremely rough estimate of mythyl based on halflife of 2-4 hours
## I am not a doctor, this is for my own personal use.
## I am not liable for any use of this program by anyone else
## see relvenent terms of the GNU 3



#could model like a nicotine patch

import numpy as np
import matplotlib.pyplot as plt


def decay(initial, t, halflife):
    return initial * (.5)**(t/halflife)


def getLevels(initial, supplementals, halflife, interval, max_time=24):
    num_sup=len(supplementals)
    times = np.arange(0,max_time,0.1)
    levels = [decay(initial, t, halflife) for t in times]
    for offset in range(1,num_sup+1):
        sup_levels =  np.zeros(interval*offset/0.1)
        sup_levels =  list(sup_levels) + [decay(supplementals[offset-1], t - interval*offset, halflife) for t in np.arange(interval*offset,max_time,0.1)]
        for i in range(len(levels)):
            levels[i] = levels[i]+sup_levels[i]


    return times, levels

init = 10
supplemental = [10,10]
spacing = 4


times0, levels0 =  getLevels(init,supplemental,2.1,spacing)
times1, levels1 =  getLevels(init,supplemental,2.5,spacing)
times2, levels2 =  getLevels(init,supplemental,2.9,spacing)
times3, levels3 =  getLevels(init,supplemental,3.3,spacing)

plt.plot(times0,levels0, 'go-',label = "half-life = 2.1")
plt.plot(times1,levels1, 'ko-',label = "half-life = 2.5")
plt.plot(times2,levels2, 'ro-',label = "half-life = 2.9")
plt.plot(times3,levels3, 'bo-',label = "half-life = 3.3")


plt.xlabel("Hours")
plt.ylabel("mg")
plt.grid()
plt.legend()
plt.show()
