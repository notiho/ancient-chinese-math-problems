"""
今有甲乙二人持錢各不知數甲得乙中半可滿四十八乙得甲大半亦滿四十八問甲乙二人元持錢各幾何
術曰如方程求之置二甲一乙錢九十六于右方置二甲三乙錢一百四十四于左方以右方二乘左方上得四中得六下得二百八十八錢以左方二乘右方上得四中得二下得九十六以右行再減左行左上空中餘四以為法下餘九十六錢為實上法下實得二十四錢為乙錢以減右下九十六餘七十二為實以右上二甲為法上法下實得三十六為甲錢也
答曰甲持錢 a 乙持錢 b 
"""

"""
Suppose there are two people, Jia and Yi, each holding an unknown amount of money.
Jia takes half of Yi's money and has a total of 48.
Yi takes more than half of Jia's money and also has a total of 48.
Question: How much money did Jia and Yi originally have?

The procedure says: Solve it as a system of equations.
Place 2 Jia and 1 Yi, totaling 96, on the right side.
Place 2 Jia and 3 Yi, totaling 144, on the left side.
Multiply the right side by 2, applying it to the left side: the top becomes 4, the middle becomes 6, and the bottom becomes 288.
Multiply the left side by 2, applying it to the right side: the top becomes 4, the middle becomes 2, and the bottom becomes 96.
Subtract the left side from the right side: the top becomes empty, the middle becomes 4, and the bottom becomes 96.
Take the middle as the divisor (4) and the bottom as the dividend (96), obtaining 24 as Yi's money.
Subtract Yi's money (24) from the right bottom (96), leaving 72 as the dividend.
Take the top of the right side (2 Jia) as the divisor, obtaining 36 as Jia's money.

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
右_倍數 = 2
左_倍數 = 2

左_新甲係數 = 左_甲係數 * 右_倍數
左_新乙係數 = 左_乙係數 * 右_倍數
左_新總錢 = 左_總錢 * 右_倍數

# 以左方二乘右方
右_新甲係數 = 右_甲係數 * 左_倍數
右_新乙係數 = 右_乙係數 * 左_倍數
右_新總錢 = 右_總錢 * 左_倍數

# 以右行再減左行
消去_甲係數 = 右_新甲係數 - 左_新甲係數
消去_乙係數 = 右_新乙係數 - 左_新乙係數
消去_總錢 = 右_新總錢 - 左_新總錢

# 中餘四以為法，下餘九十六錢為實
乙_法 = 消去_乙係數
乙_實 = 消去_總錢

# 上法下實得二十四錢為乙錢
b = Fraction(乙_實,乙_法)

# 以減右下九十六餘七十二為實
甲_實 = 右_總錢 - (右_乙係數 * b)

# 以右上二甲為法
甲_法 = 右_甲係數

# 上法下實得三十六為甲錢
a = Fraction(甲_實,甲_法)
"""
"""
