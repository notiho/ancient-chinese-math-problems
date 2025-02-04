"""
今有器中米，不知其數，前人取半，中人三分取一，後人四分取一，餘米一斗五升。問：米幾何？
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there is a container of rice, but the total amount is unknown.
The first person takes half, the second person takes one-third of what remains, and the third person takes one-fourth of what remains after that.
Finally, 1 dou and 5 sheng of rice are left.

Question: How much rice was there initially?

Answer: *a* dou.
"""

from fractions import Fraction

# Remaining rice after all the deductions
remaining_rice = 1 + Fraction(5, 10)  # 1 dou and 5 sheng = 1.5 dou

# Let the initial amount of rice be x
# After the first person takes half, (1/2) of x remains
# After the second person takes 1/3 of the remaining, (2/3) of (1/2)x remains
# After the third person takes 1/4 of the remaining, (3/4) of (2/3)(1/2)x remains
# This equals the remaining rice (1.5 dou)

# Solve for x:
# (3/4) * (2/3) * (1/2) * x = 1.5
# Simplify the fractions: (1/4) * x = 1.5
# x = 1.5 * 4 = 6

a = Fraction(6)  # Initial amount of rice in dou

# Final answer
a  # 6 dou#----- content ends here -----

"""
"""
