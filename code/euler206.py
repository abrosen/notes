"""
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
"""

# given x**2, find x
# squares only end in 0 if the number being squared does
# so 1_2_3_4_5_6_7_8_900
# or 1_2_3_4_5_6_7_8_9 *100
# the sqrt of 1_2_3_4_5_6_7_8_9 must end in 3 or 7
# 1_2_3_4_5_6_7_8_  must sumdigit %4 == 0 
# max number in search space 1929394959697989900
# sqrt(19293949596979899)
# 138902662.31062636
# so 138902662 is max
# 138902659



# less search space if we use sqrt
import math

def doTheThing():
    ans = 0
    for i in range(138902659,0,-2):
        x = str(i**2)
        if x[0::2] == '123456789':
            ans = i
            break
    print(ans*10)


if __name__ == '__main__':
    doTheThing()
