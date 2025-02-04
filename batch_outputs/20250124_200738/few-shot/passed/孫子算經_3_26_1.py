"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
術曰：如方程求之，置二甲一乙錢九十六于右方，置二甲三乙錢一百四十四于左方，以右方二乘左方，上得四，中得六，下得二百八十八錢；以左方二乘右方，上得四，中得二，下得九十六；以右行再減左行，左上空，中餘四，以為法，下餘九十六錢，為實；上法下實，得二十四錢，為乙錢，以減右下九十六，餘七十二為實，以右上二甲為法，上法下實，得三十六為甲錢也。
答曰：甲持錢 a ，乙持錢 b 。
"""

#----- content starts here -----
"""
Suppose there are two people, Jia and Yi, each holding an unknown amount of money.
If Jia takes half of Yi's money, he will have 48. If Yi takes more than half of Jia's money, he will also have 48.
Question: how much money did Jia and Yi originally have?

The procedure says: Solve it as a system of equations.
Place "2 Jia + 1 Yi = 96" on the right side, and "2 Jia + 3 Yi = 144" on the left side.
Multiply the right side by 2 and the left side by 2.
From the left side, we get: top = 4, middle = 6, bottom = 288.
From the right side, we get: top = 4, middle = 2, bottom = 96.
Subtract the right row from the left row. The top becomes empty, the middle becomes 4, and this is the divisor. The bottom becomes 96, and this is the dividend.
Divide the dividend by the divisor, obtaining 24 as Yi's money.
Subtract 24 from the right bottom (96), leaving 72 as the new dividend. Divide this by the right top (2 Jia), obtaining 36 as Jia's money.

Answer: Jia holds *a* money, Yi holds *b* money.
"""

# 置二甲一乙錢九十六于右方
右_二甲一乙 = 96

# 置二甲三乙錢一百四十四于左方
左_二甲三乙 = 144

# 以右方二乘左方
左_上 = 4  # 2 * 2甲
左_中 = 6  # 2 * 3乙
左_下 = 2 * 左_二甲三乙

# 以左方二乘右方
右_上 = 4  # 2 * 2甲
右_中 = 2  # 2 * 1乙
右_下 = 2 * 右_二甲一乙

# 以右行再減左行
法 = 左_中 - 右_中  # 中餘四
實 = 左_下 - 右_下  # 下餘九十六錢

# 上法下實，得二十四錢，為乙錢
乙 = Fraction(實, 法)

# 以減右下九十六，餘七十二為實
實_甲 = 右_下 - (右_中 * 乙)

# 以右上二甲為法，上法下實，得三十六為甲錢
甲 = Fraction(實_甲, 右_上)

a = 甲
b = 乙#----- content ends here -----

"""
"""
