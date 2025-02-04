"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

#----- content starts here -----
"""
Suppose there are four types of grain: white grain (2 bu), green grain (3 bu), yellow grain (4 bu), and black grain (5 bu). Each type of grain is less than 1 dou per bu. 
When white grain takes 1 bu from green and yellow, green grain takes 1 bu from yellow and black, yellow grain takes 1 bu from black and white, and black grain takes 1 bu from white and green, the total becomes exactly 1 dou.

Question: How much dou does each type of grain yield per bu?

Answer: White grain yields *a* dou per bu, green grain yields *b* dou per bu, yellow grain yields *c* dou per bu, and black grain yields *d* dou per bu.
"""

# Let the yield per bu for each type of grain be represented as variables:
# White grain = a dou per bu
# Green grain = b dou per bu
# Yellow grain = c dou per bu
# Black grain = d dou per bu

from fractions import Fraction

# Total bu for each type of grain
白禾 = 2
青禾 = 3
黃禾 = 4
黑禾 = 5

# The total dou becomes exactly 1 dou when the following conditions are met:
# White grain takes 1 bu from green and yellow:
# 白禾 + 青禾 + 黃禾 = 1
# Green grain takes 1 bu from yellow and black:
# 青禾 + 黃禾 + 黑禾 = 1
#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'"""
