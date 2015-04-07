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
# it's square root is 1389026623.ajfosdfja
# so 1389026620 is max



# less search space if we use sqrt
import math

print(math.sqrt(1929394959697989900))
