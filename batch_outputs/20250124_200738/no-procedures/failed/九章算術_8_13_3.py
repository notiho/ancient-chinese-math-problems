"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

#----- content starts here -----
"""
Suppose there are four types of grain: white grain (2 bu), green grain (3 bu), yellow grain (4 bu), and black grain (5 bu). Each type of grain is not full to 1 dou. 
White grain takes 1 bu each from green and yellow, green grain takes 1 bu each from yellow and black, yellow grain takes 1 bu each from black and white, and black grain takes 1 bu each from white and green. After this exchange, each type of grain becomes exactly 1 dou.

Question: How much does 1 bu of white, green, yellow, and black grain weigh in dou?

Answer: White grain per bu is *a* dou, green grain per bu is *b* dou, yellow grain per bu is *c* dou, and black grain per bu is *d* dou.
"""

from fractions import Fraction

# Define the total bu for each type of grain
白禾 = 2
青禾 = 3
黃禾 = 4
黑禾 = 5

# After the exchange, each type of grain becomes 1 dou
白禾總 = 1
青禾總 = 1
黃禾總 = 1
黑禾總 = 1

# Set up equations based on the problem:
# 白禾總 = 白禾 * a + 青禾 * b + 黃禾 * c
# 青禾總 = 青禾 * b + 黃禾 * c + 黑禾 * d
# 黃禾總 = 黃禾 * c + 黑禾 * d + 白禾 * a
# 黑禾總 = 黑禾 * d + 白禾 * a + 青禾 * b

# Solve for a, b, c, d
a = Fraction(白禾總 * 黃禾 * 黑禾 - 青禾總 * 黃禾 * 黑禾)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 0
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'"""
