"""
今有器中米，不知其數，前人取半，中人三分取一，後人四分取一，餘米一斗五升。問：米幾何？
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there is a container of rice, but the total amount is unknown.
The first person takes half, the second person takes one-third of what remains, and the third person takes one-fourth of what remains after that. Finally, 1 dou and 5 sheng of rice are left.

Question: How much rice was originally in the container?

Answer: *a* dou.
"""

from fractions import Fraction

# Remaining rice after all deductions
remaining_rice = 1 + Fraction(5, 10)  # 1 dou and 5 sheng = 1.5 dou

# Let the total amount of rice be x
# After the first person takes half, remaining = x * (1/2)
# After the second person takes 1/3 of the remaining, remaining = x * (1/2) * (2/3)
# After the third person takes 1/4 of the remaining, remaining = x * (1/2) * (2/3) * (3/4)
# Finally, the remaining rice is 1.5 dou

# Solve for x
x = remaining_rice / (Fraction(1, 2) * Fraction(2, 3) * Fraction(3, 4))

# Convert x to dou
a = x  # Total rice in dou

a  # Output the result#----- content ends here -----

"""
"""
