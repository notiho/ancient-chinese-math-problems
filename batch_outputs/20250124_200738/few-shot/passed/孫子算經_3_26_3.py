"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
術曰：如方程求之，置二甲一乙錢九十六于右方，置二甲三乙錢一百四十四于左方，以右方二乘左方，上得四，中得六，下得二百八十八錢；以左方二乘右方，上得四，中得二，下得九十六；以右行再減左行，左上空，中餘四，以為法，下餘九十六錢，為實；上法下實，得二十四錢，為乙錢，以減右下九十六，餘七十二為實，以右上二甲為法，上法下實，得三十六為甲錢也。
答曰：甲持錢 a ，乙持錢 b 。
"""

#----- content starts here -----
"""
Suppose there are two people, Jia and Yi, each holding an unknown amount of money.
If Jia takes half of Yi's money, he will have 48.
If Yi takes more than half of Jia's money, he will also have 48.
Question: how much money did Jia and Yi originally have?

The procedure says: Solve it as a system of equations.
Place "2 Jia + 1 Yi = 96" on the right side.
Place "2 Jia + 3 Yi = 144" on the left side.
Multiply the right side by 2 and the left side by 2:
The left side becomes 4, 6, and 288.
The right side becomes 4, 2, and 96.
Subtract the left side from the right side:
The top becomes empty, the middle becomes 4, and the bottom becomes 96.
The middle (4) becomes the divisor, and the bottom (96) becomes the dividend.
Divide the dividend by the divisor to get 24, which is Yi's money.
Subtract Yi's money (24) from the right bottom (96), leaving 72.
Use the top right (2 Jia) as the divisor and the remaining 72 as the dividend.
Divide the dividend by the divisor to get 36, which is Jia's money.

Answer: Jia originally had *a* money, and Yi originally had *b* money.
"""

# 置二甲一乙錢九十六于右方
右_甲係數 = 2
右_乙係數 = 1
右_常數 = 96

# 置二甲三乙錢一百四十四于左方
左_甲係數 = 2
左_乙係數 = 3
左_常數 = 144

# 以右方二乘左方
左_甲係數 *= 2
左_乙係數 *= 2
左_常數 *= 2

# 上得四，中得六，下得二百八十八錢
左_甲係數 = 4
左_乙係數 = 6
左_常數 = 288

# 以左方二乘右方
右_甲係數 *= 2
右_乙係數 *= 2
右_常數 *= 2

# 上得四，中得二，下得九十六
右_甲係數 = 4
右_乙係數 = 2
右_常數 = 192

# 以右行再減左行
法_乙係數 = 右_乙係數 - 左_乙係數
法_常數 = 右_常數 - 左_常數

# 左上空，中餘四，以為法
法 = 法_乙係數

# 下餘九十六錢，為實
實 = 法_常數

# 上法下實，得二十四錢，為乙錢
b = Fraction(實, 法)

# 以減右下九十六，餘七十二為實
實 = 右_常數 - (右_乙係數 * b)

# 以右上二甲為法
法 = 右_甲係數

# 上法下實，得三十六為甲錢
a = Fraction(實, 法)#----- content ends here -----

"""
"""
