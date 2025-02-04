"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
術曰：如方程求之，置二甲一乙錢九十六于右方，置二甲三乙錢一百四十四于左方，以右方二乘左方，上得四，中得六，下得二百八十八錢；以左方二乘右方，上得四，中得二，下得九十六；以右行再減左行，左上空，中餘四，以為法，下餘九十六錢，為實；上法下實，得二十四錢，為乙錢，以減右下九十六，餘七十二為實，以右上二甲為法，上法下實，得三十六為甲錢也。
答曰：甲持錢 a ，乙持錢 b 。
"""

"""
Suppose there are two people, Jia and Yi, each holding an unknown amount of money.
If Jia takes half of Yi's money, he will have 48. 
If Yi takes more than half of Jia's money, he will also have 48.
Question: how much money do Jia and Yi originally hold?

The procedure says: Solve it as a system of equations.
Place "2 Jia + 1 Yi = 96" on the right side, and "2 Jia + 3 Yi = 144" on the left side.
Multiply the right side by 2 and the left side by 2:
- From the left side, the top becomes 4, the middle becomes 6, and the bottom becomes 288.
- From the right side, the top becomes 4, the middle becomes 2, and the bottom becomes 192.
Subtract the right side from the left side:
- The top becomes empty, the middle becomes 4, and the bottom becomes 96.
The middle (4) becomes the divisor, and the bottom (96) becomes the dividend.
Divide the dividend by the divisor, obtaining 24 as Yi's money.
Subtract Yi's money (24) from the original total (96), leaving 72.
Divide this by the coefficient of Jia (2), obtaining 36 as Jia's money.

Answer: Jia holds *a* money, and Yi holds *b* money.
"""

from fractions import Fraction

# Step 1: Define the equations
# Equation 1: 2甲 + 1乙 = 96
# Equation 2: 2甲 + 3乙 = 144

# Step 2: Multiply both equations by 2
# For Equation 1: 2 * (2甲 + 1乙) = 2 * 96
左上 = 4  # Coefficient of 甲 in Equation 1
左中 = 2  # Coefficient of 乙 in Equation 1
左下 = 192  # Constant in Equation 1

# For Equation 2: 2 * (2甲 + 3乙) = 2 * 144
右上 = 4  # Coefficient of 甲 in Equation 2
右中 = 6  # Coefficient of 乙 in Equation 2
右下 = 288  # Constant in Equation 2

# Step 3: Subtract the right equation from the left equation
# (4甲 + 6乙 - 4甲 - 2乙 = 288 - 192)
法 = 右中 - 左中  # Coefficient of 乙 after subtraction
實 = 右下 - 左下  # Constant after subtraction

# Step 4: Solve for 乙
乙 = Fraction(實, 法)

# Step 5: Substitute 乙 back into Equation 1 to solve for 甲
# 2甲 + 1乙 = 96
甲 = Fraction(左下 - 左中 * 乙, 左上)

# Final results
a = 甲
b = 乙
"""
"""
