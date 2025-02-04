"""
今有甲乙二人持錢各不知數甲得乙中半可滿四十八乙得甲大半亦滿四十八問甲乙二人元持錢各幾何
術曰如方程求之置二甲一乙錢九十六于右方置二甲三乙錢一百四十四于左方以右方二乘左方上得四中得六下得二百八十八錢以左方二乘右方上得四中得二下得九十六以右行再減左行左上空中餘四以為法下餘九十六錢為實上法下實得二十四錢為乙錢以減右下九十六餘七十二為實以右上二甲為法上法下實得三十六為甲錢也
答曰甲持錢 a 乙持錢 b 
"""

#----- content starts here -----
"""
Suppose there are two people, Jia and Yi, each holding an unknown amount of money.
Jia takes half of Yi's money and has a total of 48.
Yi takes more than half of Jia's money and also has a total of 48.
Question: How much money did Jia and Yi originally have?

The procedure says: Solve it as a system of equations.
Place 2 Jia and 1 Yi with a total of 96 on the right side.
Place 2 Jia and 3 Yi with a total of 144 on the left side.
Multiply the right side by 2 and apply it to the left side: the top becomes 4, the middle becomes 6, and the bottom becomes 288.
Multiply the left side by 2 and apply it to the right side: the top becomes 4, the middle becomes 2, and the bottom becomes 96.
Subtract the left side from the right side. The top becomes empty, the middle becomes 4, and the bottom becomes 96. Use the middle as the divisor and the bottom as the dividend.
Divide the bottom by the middle to get 24, which is Yi's money.
Subtract Yi's money from the right bottom (96), leaving 72 as the dividend.
Use the top of the right side (2 Jia) as the divisor.
Divide the dividend by the divisor to get 36, which is Jia's money.

Answer: Jia originally had *a* money, and Yi originally had *b* money.
"""

# 置二甲一乙錢九十六于右方
右_甲係數 = 2
右_乙係數 = 1
右_總錢 = 96

# 置二甲三乙錢一百四十四于左方
左_甲係數 = 2
左_乙係數 = 3
左_總錢 = 144

# 以右方二乘左方
左_甲係數 *= 2
左_乙係數 *= 2
左_總錢 *= 2

# 得四中得六下得二百八十八錢
左_甲係數 = 4
左_乙係數 = 6
左_總錢 = 288

# 以左方二乘右方
右_甲係數 *= 2
右_乙係數 *= 2
右_總錢 *= 2

# 得四中得二下得九十六
右_甲係數 = 4
右_乙係數 = 2
右_總錢 = 96

# 以右行再減左行
中_乙係數 = 右_乙係數 - 左_乙係數
下_總錢 = 右_總錢 - 左_總錢

# 左上空中餘四以為法
法 = 中_乙係數

# 下餘九十六錢為實
實 = abs(下_總錢)

# 上法下實得二十四錢為乙錢
b = Fraction(實, 法)

# 以減右下九十六餘七十二為實
實 = 右_總錢 - (右_乙係數 * b)

# 以右上二甲為法
法 = 右_甲係數

# 上法下實得三十六為甲錢
a = Fraction(實, 法)

# 答曰甲持錢 a 乙持錢 b
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 36, Actual: 48
Variable 'b' has wrong value. Expected: 24, Actual: -48"""
