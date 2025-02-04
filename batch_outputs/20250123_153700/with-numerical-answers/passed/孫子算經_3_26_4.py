"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
術曰：如方程求之，置二甲一乙錢九十六于右方，置二甲三乙錢一百四十四于左方，以右方二乘左方，上得四，中得六，下得二百八十八錢；以左方二乘右方，上得四，中得二，下得九十六；以右行再減左行，左上空，中餘四，以為法，下餘九十六錢，為實；上法下實，得二十四錢，為乙錢，以減右下九十六，餘七十二為實，以右上二甲為法，上法下實，得三十六為甲錢也。
答曰：甲持錢 a(=36) ，乙持錢 b(=24) 。
"""

"""
Suppose there are two people, Jia and Yi, each holding an unknown amount of money.
Jia takes half of Yi's money and has a total of 48.
Yi takes more than half of Jia's money and also has a total of 48.
Question: how much money did Jia and Yi originally have?

The procedure says: Solve it as a system of equations.
Place "2 Jia + 1 Yi = 96" on the right side, and "2 Jia + 3 Yi = 144" on the left side.
Multiply the right side by 2 and the left side by 2.
For the left side, the top becomes 4, the middle becomes 6, and the bottom becomes 288.
For the right side, the top becomes 4, the middle becomes 2, and the bottom becomes 96.
Subtract the right row from the left row.
The left top becomes empty, the middle becomes 4, which is the divisor, and the bottom becomes 96, which is the dividend.
Divide the dividend by the divisor, obtaining 24, which is Yi's money.
Subtract this from the right bottom 96, leaving 72 as the dividend.
For the right top "2 Jia," use it as the divisor.
Divide the dividend by the divisor, obtaining 36, which is Jia's money.

Answer: Jia originally had *a*(=36), and Yi originally had *b*(=24).
"""

from fractions import Fraction

# Step 1: Define the equations
# 2甲 + 1乙 = 96
# 2甲 + 3乙 = 144

# Step 2: Multiply the equations
# Multiply the first equation by 2
右上 = 2 * 2  # 4
右中 = 2 * 1  # 2
右下 = 2 * 96  # 192

# Multiply the second equation by 2
左上 = 2 * 2  # 4
左中 = 2 * 3  # 6
左下 = 2 * 144  # 288

# Step 3: Subtract the right equation from the left equation
法 = 左中 - 右中  # 6 - 2 = 4
實 = 左下 - 右下  # 288 - 192 = 96

# Step 4: Solve for Yi's money
乙 = Fraction(實, 法)  # 96 / 4 = 24

# Step 5: Solve for Jia's money
實 = 右下 - (右中 * 乙)  # 192 - (2 * 24) = 144
法 = 右上  # 2
甲 = Fraction(實, 法)  # 144 / 2 = 36

# Final results
a = 甲  # 36
b = 乙  # 24
"""
"""
