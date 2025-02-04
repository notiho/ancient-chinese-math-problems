"""
今有兵六千七百九十二人人給米二升問一日一月一年各幾何
術曰置兵數以二因之得一日之數上十之得十日之數以三因之得一月之數以十二因之得一年之數
答曰一日 a斛 一月 b斛 一年 c斛
"""

#----- content starts here -----
"""
Suppose there are 6792 soldiers, and each is given 2 sheng of rice per day.
Question: how much rice is needed for one day, one month, and one year?

The procedure says: Place the number of soldiers. Multiply it by 2 to obtain the amount for one day.
Multiply it by 10 to obtain the amount for ten days.
Multiply it by 3 to obtain the amount for one month.
Multiply it by 12 to obtain the amount for one year.

Answer: one day requires *a* hu, one month requires *b* hu, and one year requires *c* hu.
"""

# 兵六千七百九十二人
兵數 = 6792

# 每人每日米二升
每日每人米 = 2  # 升

# 置兵數，以二因之，得一日之數
一日米升 = 兵數 * 每日每人米

# 升轉換為斛 (1 斛 = 10 升)
一日米斛 = Fraction(一日米升, 10)

# 上十之，得十日之數 (not directly needed here)

# 以三因之，得一月之數
一月米升 = 一日米升 * 30
一月米斛 = Fraction(一月米升, 10)

# 以十二因之，得一年之數
一年米升 = 一日米升 * 365
一年米斛 = Fraction(一年米升, 10)

# 答案
a = 一日米斛
b = 一月米斛
c = 一年米斛#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 3396/25, Actual: 6792/5
Variable 'b' has wrong value. Expected: 20376/5, Actual: 40752
Variable 'c' has wrong value. Expected: 244512/5, Actual: 495816"""
