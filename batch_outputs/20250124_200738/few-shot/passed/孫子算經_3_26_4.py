"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
術曰：如方程求之，置二甲一乙錢九十六于右方，置二甲三乙錢一百四十四于左方，以右方二乘左方，上得四，中得六，下得二百八十八錢；以左方二乘右方，上得四，中得二，下得九十六；以右行再減左行，左上空，中餘四，以為法，下餘九十六錢，為實；上法下實，得二十四錢，為乙錢，以減右下九十六，餘七十二為實，以右上二甲為法，上法下實，得三十六為甲錢也。
答曰：甲持錢 a ，乙持錢 b 。
"""

#----- content starts here -----
"""
Suppose there are two people, Jia and Yi, each holding an unknown amount of money.
If Jia takes half of Yi's money, he will have 48. If Yi takes more than half of Jia's money, he will also have 48.
Question: how much money did Jia and Yi originally hold?

The procedure says: Solve it as a system of equations.
Place "2 Jia + 1 Yi = 96" on the right side, and "2 Jia + 3 Yi = 144" on the left side.
Multiply the right side by 2 and the left side by 2.
From the left side, the top becomes 4, the middle becomes 6, and the bottom becomes 288.
From the right side, the top becomes 4, the middle becomes 2, and the bottom becomes 96.
Subtract the right row from the left row. The left top becomes empty, the middle becomes 4, which is the divisor, and the bottom becomes 96, which is the dividend.
Divide the dividend by the divisor, obtaining 24, which is Yi's money.
Subtract this from the right bottom (96), leaving 72 as the dividend.
Divide this by the right top (2 Jia), obtaining 36, which is Jia's money.

Answer: Jia holds *a* money, and Yi holds *b* money.
"""

# 置二甲一乙錢九十六于右方
右方_甲系數 = 2
右方_乙系數 = 1
右方_常數 = 96

# 置二甲三乙錢一百四十四于左方
左方_甲系數 = 2
左方_乙系數 = 3
左方_常數 = 144

# 以右方二乘左方
左方_甲系數 *= 2
左方_乙系數 *= 2
左方_常數 *= 2

# 上得四，中得六，下得二百八十八錢
左方_甲系數 = 4
左方_乙系數 = 6
左方_常數 = 288

# 以左方二乘右方
右方_甲系數 *= 2
右方_乙系數 *= 2
右方_常數 *= 2

# 上得四，中得二，下得九十六
右方_甲系數 = 4
右方_乙系數 = 2
右方_常數 = 192

# 以右行再減左行
法 = 左方_乙系數 - 右方_乙系數
實 = 左方_常數 - 右方_常數

# 上法下實，得二十四錢，為乙錢
b = Fraction(實, 法)

# 以減右下九十六，餘七十二為實
實 = 右方_常數 - (右方_乙系數 * b)

# 以右上二甲為法，上法下實，得三十六為甲錢
a = Fraction(實, 右方_甲系數)#----- content ends here -----

"""
"""
