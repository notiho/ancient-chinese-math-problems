"""
今有甲乙二人持錢各不知數甲得乙中半可滿四十八乙得甲大半亦滿四十八問甲乙二人元持錢各幾何
術曰如方程求之置二甲一乙錢九十六于右方置二甲三乙錢一百四十四于左方以右方二乘左方上得四中得六下得二百八十八錢以左方二乘右方上得四中得二下得九十六以右行再減左行左上空中餘四以為法下餘九十六錢為實上法下實得二十四錢為乙錢以減右下九十六餘七十二為實以右上二甲為法上法下實得三十六為甲錢也
答曰甲持錢 a 乙持錢 b 
"""

"""
Suppose there are two people, Jia and Yi, each holding an unknown amount of money.
Jia takes half of Yi's money and has a total of 48.
Yi takes more than half of Jia's money and also has a total of 48.
Question: how much money did Jia and Yi originally have?

The procedure says: Solve it as a system of equations.
Place 2 Jia and 1 Yi [as coefficients] with 96 on the right-hand side.
Place 2 Jia and 3 Yi [as coefficients] with 144 on the left-hand side.
Multiply the right-hand side by 2 and the left-hand side by 2.
For the left-hand side, multiply the top by 2, the middle by 6, and the bottom by 288.
For the right-hand side, multiply the top by 2, the middle by 4, and the bottom by 96.
Subtract the right-hand side from the left-hand side.
The top becomes empty, the middle leaves 4 as the divisor, and the bottom leaves 96 as the dividend.
Divide the dividend by the divisor to get 24, which is Yi's money.
Subtract this from the right-hand side's bottom (96), leaving 72 as the dividend.
Divide this by the right-hand side's top (2 Jia) to get 36, which is Jia's money.

Answer: Jia originally had *a* money, and Yi originally had *b* money.
"""

# 置二甲一乙錢九十六于右方
右方_甲係數 = 2
右方_乙係數 = 1
右方_常數 = 96

# 置二甲三乙錢一百四十四于左方
左方_甲係數 = 2
左方_乙係數 = 3
左方_常數 = 144

# 以右方二乘左方
左方_甲係數 *= 2
左方_乙係數 *= 2
左方_常數 *= 2

# 以左方二乘右方
右方_甲係數 *= 2
右方_乙係數 *= 2
右方_常數 *= 2

# 右行再減左行
甲係數 = 右方_甲係數 - 左方_甲係數
乙係數 = 右方_乙係數 - 左方_乙係數
常數 = 右方_常數 - 左方_常數

# 中餘四以為法，下餘九十六錢為實
法 = abs(乙係數)
實 = abs(常數)

# 上法下實得二十四錢為乙錢
b = Fraction(實, 法)

# 以減右下九十六餘七十二為實
實 = 右方_常數 // 2 - b

# 以右上二甲為法，上法下實得三十六為甲錢
a = Fraction(實, 右方_甲係數 // 2)

# 答案
a, b
"""
"""
