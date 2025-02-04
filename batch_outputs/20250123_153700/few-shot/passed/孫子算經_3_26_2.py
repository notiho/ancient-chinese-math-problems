"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
術曰：如方程求之，置二甲一乙錢九十六于右方，置二甲三乙錢一百四十四于左方，以右方二乘左方，上得四，中得六，下得二百八十八錢；以左方二乘右方，上得四，中得二，下得九十六；以右行再減左行，左上空，中餘四，以為法，下餘九十六錢，為實；上法下實，得二十四錢，為乙錢，以減右下九十六，餘七十二為實，以右上二甲為法，上法下實，得三十六為甲錢也。
答曰：甲持錢 a ，乙持錢 b 。
"""

"""
Suppose there are two people, A (Jia) and B (Yi), each holding an unknown amount of money.
If A takes half of B's money, A will have 48.
If B takes more than half of A's money, B will also have 48.
Question: How much money did A and B originally hold?

The procedure says: Solve it as a system of equations.
Place "2A + 1B = 96" on the right side and "2A + 3B = 144" on the left side.
Multiply the right side by 2 and the left side by 2.
From the right side: top = 4, middle = 6, bottom = 288.
From the left side: top = 4, middle = 2, bottom = 96.
Subtract the left row from the right row: the left top becomes empty, the middle becomes 4 (as the divisor), and the bottom becomes 96 (as the dividend).
Divide the dividend by the divisor, obtaining 24 as B's money.
Subtract this from the right bottom (96), leaving 72 as the new dividend.
Divide this by the right top (2A), obtaining 36 as A's money.

Answer: A holds *a* money, and B holds *b* money.
"""

# Define the equations:
# 2甲 + 乙 = 96
# 2甲 + 3乙 = 144

# Step 1: Multiply the right equation by 2
右上 = 2 * 2  # 2甲 becomes 4甲
右中 = 2 * 1  # 乙 becomes 2乙
右下 = 2 * 96  # 96 becomes 192

# Step 2: Multiply the left equation by 2
左上 = 2 * 2  # 2甲 becomes 4甲
左中 = 2 * 3  # 3乙 becomes 6乙
左下 = 2 * 144  # 144 becomes 288

# Step 3: Subtract the left row from the right row
上法 = 右上 - 左上  # 4甲 - 4甲 = 0
中法 = 右中 - 左中  # 2乙 - 6乙 = -4乙
下實 = 右下 - 左下  # 192 - 288 = -96

# Step 4: Solve for 乙 (B's money)
b = Fraction(-下實, -中法)  # -96 / -4 = 24

# Step 5: Substitute B's money into the right equation to solve for A
下實 = 96 - b  # 96 - 24 = 72
上法 = 2  # 2甲
a = Fraction(下實, 上法)  # 72 / 2 = 36

# Final answer
a = 36  # A's money
b = 24  # B's money
"""
"""
