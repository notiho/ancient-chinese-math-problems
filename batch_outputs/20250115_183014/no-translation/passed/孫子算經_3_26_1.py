"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
術曰：如方程求之，置二甲一乙錢九十六于右方，置二甲三乙錢一百四十四于左方，以右方二乘左方，上得四，中得六，下得二百八十八錢；以左方二乘右方，上得四，中得二，下得九十六；以右行再減左行，左上空，中餘四，以為法，下餘九十六錢，為實；上法下實，得二十四錢，為乙錢，以減右下九十六，餘七十二為實，以右上二甲為法，上法下實，得三十六為甲錢也。
答曰：甲持錢 a ，乙持錢 b 。
"""

"""

"""


from fractions import Fraction

# 置二甲一乙錢九十六于右方
右上 = 2  # 2甲
右中 = 1  # 1乙
右下 = 96  # 96錢

# 置二甲三乙錢一百四十四于左方
左上 = 2  # 2甲
左中 = 3  # 3乙
左下 = 144  # 144錢

# 以右方二乘左方
左上_乘 = 右上 * 左上  # 上得四
左中_乘 = 右上 * 左中  # 中得六
左下_乘 = 右上 * 左下  # 下得二百八十八錢

# 以左方二乘右方
右上_乘 = 左上 * 右上  # 上得四
右中_乘 = 左上 * 右中  # 中得二
右下_乘 = 左上 * 右下  # 下得九十六

# 以右行再減左行
法上 = 右上_乘 - 左上_乘  # 左上空
法中 = 右中_乘 - 左中_乘  # 中餘四
法下 = 右下_乘 - 左下_乘  # 下餘九十六錢

# 左中餘四，以為法
法 = 法中  # 法 = 4

# 下餘九十六錢，為實
實 = 法下  # 實 = 96

# 上法下實，得二十四錢，為乙錢
b = Fraction(實, 法)  # 乙錢 = 24

# 以減右下九十六，餘七十二為實
實_甲 = 右下 - (右中 * b)  # 實_甲 = 72

# 以右上二甲為法
法_甲 = 右上  # 法_甲 = 2

# 上法下實，得三十六為甲錢
a = Fraction(實_甲, 法_甲)  # 甲錢 = 36


"""
 

答曰：甲持錢 `a = 36` ，乙持錢 `b = 24` 。
"""


"""
"""
