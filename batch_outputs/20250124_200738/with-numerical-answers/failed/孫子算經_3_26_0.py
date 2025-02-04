"""
今有甲乙二人持錢，各不知數。甲得乙中半，可滿四十八；乙得甲大半，亦滿四十八。問：甲乙二人元持錢各幾何？
術曰：如方程求之，置二甲一乙錢九十六于右方，置二甲三乙錢一百四十四于左方，以右方二乘左方，上得四，中得六，下得二百八十八錢；以左方二乘右方，上得四，中得二，下得九十六；以右行再減左行，左上空，中餘四，以為法，下餘九十六錢，為實；上法下實，得二十四錢，為乙錢，以減右下九十六，餘七十二為實，以右上二甲為法，上法下實，得三十六為甲錢也。
答曰：甲持錢 a(=36) ，乙持錢 b(=24) 。
"""

#----- content starts here -----
"""
Suppose there are two people, Jia and Yi, each holding an unknown amount of money.
If Jia takes half of Yi's money, he will have 48. 
If Yi takes more than half of Jia's money, he will also have 48.
Question: how much money did Jia and Yi originally have?

The procedure says: Solve it as a system of equations.
Place "2 Jia + 1 Yi = 96" on the right side, and "2 Jia + 3 Yi = 144" on the left side.
Multiply the right side by 2 and the left side by 2.
For the left side, the top becomes 4, the middle becomes 6, and the bottom becomes 288.
For the right side, the top becomes 4, the middle becomes 2, and the bottom becomes 96.
Subtract the right row from the left row. The top becomes empty, the middle becomes 4, and the bottom becomes 96, which is the divisor.
Divide the bottom by the divisor to get 24, which is Yi's money.
Subtract Yi's money from the right bottom (96), leaving 72 as the remainder.
Divide the remainder by the right top (2 Jia), obtaining 36, which is Jia's money.

Answer: Jia has *a*(=36), and Yi has *b*(=24).
"""

# 置二甲一乙錢九十六于右方
右上 = 2  # 2 Jia
右中 = 1  # 1 Yi
右下 = 96  # Total = 96

# 置二甲三乙錢一百四十四于左方
左上 = 2  # 2 Jia
左中 = 3  # 3 Yi
左下 = 144  # Total = 144

# 以右方二乘左方
左上 *= 2  # 4 Jia
左中 *= 2  # 6 Yi
左下 *= 2  # 288

# 以左方二乘右方
右上 *= 2  # 4 Jia
右中 *= 2  # 2 Yi
右下 *= 2  # 192

# 以右行再減左行
法中 = 左中 - 右中  # 6 - 2 = 4
法下 = 左下 - 右下  # 288 - 192 = 96

# 上法下實，得二十四錢，為乙錢
乙錢 = Fraction(法下, 法中)  # 96 / 4 = 24

# 以減右下九十六，餘七十二為實
實 = 右下 // 2 - 乙錢#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
