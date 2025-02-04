"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
術曰：如方程求之，置二甲一乙錢九十六于右方，置二甲三乙錢一百四十四于左方，以右方二乘左方，上得四，中得六，下得二百八十八錢；以左方二乘右方，上得四，中得二，下得九十六；以右行再減左行，左上空，中餘四，以為法，下餘九十六錢，為實；上法下實，得二十四錢，為乙錢，以減右下九十六，餘七十二為實，以右上二甲為法，上法下實，得三十六為甲錢也。
答曰：甲持錢 a ，乙持錢 b 。
"""

#----- content starts here -----
"""
Suppose there are two people, A (Jia) and B (Yi), each holding an unknown amount of money.
If A takes half of B's money, A will have 48. 
If B takes more than half of A's money, B will also have 48.
Question: How much money did A and B originally have?

The procedure says: Solve it as a system of equations.
Place "2A + B = 96" on the right-hand side, and "2A + 3B = 144" on the left-hand side.
Multiply the right-hand side by 2, and the left-hand side by 2.
Subtract the left-hand side from the right-hand side to isolate B.
Solve for B, then substitute back to solve for A.

Answer: A originally had *a* money, and B originally had *b* money.
"""

from fractions import Fraction

# Define the equations:
# 2A + B = 96
# 2A + 3B = 144

# Step 1: Eliminate 2A by subtracting the equations
# Multiply the first equation by 2:
# 4A + 2B = 192
# The second equation remains:
# 4A + 6B = 288

# Subtract the first equation from the second:
# (4A + 6B) - (4A + 2B) = 288 - 192
# 4B = 96
b = Fraction(96, 4)

# Step 2: Substitute B into the first equation to solve for A
# 2A + B = 96
# 2A + 24 = 96
# 2A = 96 - 24
# 2A = 72
a = Fraction(72, 2)

# Final Answer
print(f"A originally had {a} money.")
print(f"B originally had {b} money.")

# Answer:
# a = 36
# b = 24#----- content ends here -----

"""
"""
