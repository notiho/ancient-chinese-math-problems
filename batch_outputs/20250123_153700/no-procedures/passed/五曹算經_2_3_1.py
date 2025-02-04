"""
今有兵三千八百三十七人，人給錢五百五十六文。問：計㡬何？
答曰： a貫 。
"""

"""
Suppose there are 3,837 soldiers, and each soldier is given 556 wen (a unit of currency).
Question: how many guan (strings of 1,000 wen) are required in total?

Answer: *a* guan.
"""

# Number of soldiers
兵 = 3837

# Money given to each soldier in wen
每人錢 = 556

# Total money in wen
總錢 = 兵 * 每人錢

# Convert wen to guan (1 guan = 1000 wen)
a = Fraction(總錢, 1000)
"""
"""
