"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
術曰：如方程求之，置二甲一乙錢九十六于右方，置二甲三乙錢一百四十四于左方，以右方二乘左方，上得四，中得六，下得二百八十八錢；以左方二乘右方，上得四，中得二，下得九十六；以右行再減左行，左上空，中餘四，以為法，下餘九十六錢，為實；上法下實，得二十四錢，為乙錢，以減右下九十六，餘七十二為實，以右上二甲為法，上法下實，得三十六為甲錢也。
答曰：甲持錢 a(=36) ，乙持錢 b(=24) 。
"""

"""
Suppose there are two people, Jia and Yi, each holding an unknown amount of money.
Jia takes half of Yi's money and has a total of 48. Yi takes more than half of Jia's money and also has a total of 48.
Question: how much money did Jia and Yi originally have?

The procedure says: Solve it like a system of equations.
Place 2 Jia and 1 Yi totaling 96 on the right side.
Place 2 Jia and 3 Yi totaling 144 on the left side.
Multiply the right side by 2 and the left side by 2.
From the left side, the top is 4, the middle is 6, and the bottom is 288.
From the right side, the top is 4, the middle is 2, and the bottom is 96.
Subtract the right row from the left row twice.
The left top becomes empty, the middle becomes 4, and this is the divisor.
The bottom becomes 96, and this is the dividend.
Divide the dividend by the divisor, obtaining 24 as Yi's money.
Subtract this from the right bottom 96, leaving 72 as the dividend.
Divide this by the right top 2 Jia, obtaining 36 as Jia's money.

Answer: Jia holds *a*(=36), and Yi holds *b*(=24).
"""

# 置二甲一乙錢九十六于右方
右上 = 2  # 2 Jia
右中 = 1  # 1 Yi
右下 = 96  # Total money

# 置二甲三乙錢一百四十四于左方
左上 = 2  # 2 Jia
左中 = 3  # 3 Yi
左下 = 144  # Total money

# 以右方二乘左方
左上 *= 2
左中 *= 2
左下 *= 2

# 上得四，中得六，下得二百八十八錢
左上 = 4
左中 = 6
左下 = 288

# 以左方二乘右方
右上 *= 2
右中 *= 2
右下 *= 2

# 上得四，中得二，下得九十六
右上 = 4
右中 = 2
右下 = 96

# 以右行再減左行
# 左上空，中餘四，以為法
法 = 左中 - 右中

# 下餘九十六錢，為實
實 = 左下 - 右下

# 上法下實，得二十四錢，為乙錢
b = Fraction(實, 法)  # Yi's money = 24

# 以減右下九十六，餘七十二為實
實 = 右下 - (右中 * b)

# 以右上二甲為法
法 = 右上

# 上法下實，得三十六為甲錢
a = Fraction(實, 法)  # Jia's money = 36
"""
Variable 'a' has wrong value. Expected: 36, Actual: 0
Variable 'b' has wrong value. Expected: 24, Actual: 48"""
