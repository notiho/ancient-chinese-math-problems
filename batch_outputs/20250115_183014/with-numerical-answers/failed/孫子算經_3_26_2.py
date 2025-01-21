"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
術曰：如方程求之，置二甲一乙錢九十六于右方，置二甲三乙錢一百四十四于左方，以右方二乘左方，上得四，中得六，下得二百八十八錢；以左方二乘右方，上得四，中得二，下得九十六；以右行再減左行，左上空，中餘四，以為法，下餘九十六錢，為實；上法下實，得二十四錢，為乙錢，以減右下九十六，餘七十二為實，以右上二甲為法，上法下實，得三十六為甲錢也。
答曰：甲持錢 a(=36) ，乙持錢 b(=24) 。
"""

"""
Suppose there are two people, Jia and Yi, each holding an unknown amount of money.
If Jia takes half of Yi's money, he will have 48 coins.
If Yi takes more than half of Jia's money, he will also have 48 coins.
Question: how much money did Jia and Yi originally hold?

The procedure says: Solve it as a system of equations.
Place "2 Jia + 1 Yi = 96" on the right side, and "2 Jia + 3 Yi = 144" on the left side.
Multiply the right side by 2, and the left side by 2.
From the right side, the top is 4, the middle is 6, and the bottom is 288 coins.
From the left side, the top is 4, the middle is 2, and the bottom is 96 coins.
Subtract the left row from the right row.
The top becomes empty, the middle becomes 4, which is the divisor, and the bottom becomes 96 coins, which is the dividend.
Divide the dividend by the divisor, obtaining 24 coins, which is Yi's money.
Subtract Yi's money from the right bottom (96), leaving 72 coins as the dividend.
Divide the dividend by the right top (2 Jia), obtaining 36 coins, which is Jia's money.

Answer: Jia holds *a*(=36) coins, and Yi holds *b*(=24) coins.
"""

# 置二甲一乙錢九十六于右方
右方_甲 = 2
右方_乙 = 1
右方_錢 = 96

# 置二甲三乙錢一百四十四于左方
左方_甲 = 2
左方_乙 = 3
左方_錢 = 144

# 以右方二乘左方
右乘左_甲 = 右方_甲 * 2
右乘左_乙 = 右方_乙 * 2
右乘左_錢 = 右方_錢 * 2

# 上得四，中得六，下得二百八十八錢
右乘左_甲 = 4
右乘左_乙 = 6
右乘左_錢 = 288

# 以左方二乘右方
左乘右_甲 = 左方_甲 * 2
左乘右_乙 = 左方_乙 * 2
左乘右_錢 = 左方_錢 * 2

# 上得四，中得二，下得九十六
左乘右_甲 = 4
左乘右_乙 = 2
左乘右_錢 = 96

# 以右行再減左行
減_甲 = 右乘左_甲 - 左乘右_甲
減_乙 = 右乘左_乙 - 左乘右_乙
減_錢 = 右乘左_錢 - 左乘右_錢

# 左上空，中餘四，以為法
法 = 減_乙

# 下餘九十六錢，為實
實 = 減_錢

# 上法下實，得二十四錢，為乙錢
乙錢 = Fraction(實, 法) # 24

# 以減右下九十六，餘七十二為實
實 = 右方_錢 - (右方_乙 * 乙錢)

# 以右上二甲為法
法 = 右方_甲

# 上法下實，得三十六為甲錢
甲錢 = Fraction(實, 法) # 36

a = 甲錢 # 36
b = 乙錢 # 24
"""
Variable 'a' has wrong value. Expected: 36, Actual: 24
Variable 'b' has wrong value. Expected: 24, Actual: 48"""
