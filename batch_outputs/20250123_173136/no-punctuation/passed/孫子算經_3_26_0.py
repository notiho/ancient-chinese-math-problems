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
Place 2 Jia and 1 Yi's money as 96 on the right side.
Place 2 Jia and 3 Yi's money as 144 on the left side.
Multiply the right side by 2 and the left side by 2.
Subtract the left side from the right side, leaving 4 in the middle as the divisor (法) and 96 as the dividend (實).
Divide the dividend by the divisor to get 24, which is Yi's money.
Subtract Yi's money from the total on the right side to get 72, which is Jia's money.

Answer: Jia originally had *a* money, and Yi originally had *b* money.
"""

# 置二甲一乙錢九十六于右方
右甲係數 = 2
右乙係數 = 1
右總錢 = 96

# 置二甲三乙錢一百四十四于左方
左甲係數 = 2
左乙係數 = 3
左總錢 = 144

# 以右方二乘左方
左上 = 左甲係數 * 右甲係數
左中 = 左乙係數 * 右甲係數
左下 = 左總錢 * 右甲係數

# 得四中得六下得二百八十八錢
左上 = 左上
左中 = 左中
左下 = 左下

# 以左方二乘右方
右上 = 右甲係數 * 左甲係數
右中 = 右乙係數 * 左甲係數
右下 = 右總錢 * 左甲係數

# 得四中得二下得九十六
右上 = 右上
右中 = 右中
右下 = 右下

# 以右行再減左行
法 = 右中 - 左中
實 = 右下 - 左下

# 左上空中餘四以為法
法 = 法

# 下餘九十六錢為實
實 = 實

# 上法下實得二十四錢為乙錢
b = Fraction(實, 法)

# 以減右下九十六餘七十二為實
實 = 右總錢 - b

# 以右上二甲為法
法 = 右甲係數

# 上法下實得三十六為甲錢
a = Fraction(實, 法)

# 答曰甲持錢 a 乙持錢 b
"""
"""
