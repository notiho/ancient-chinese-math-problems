"""
今有布一匹，價直一百二十五。今有布二丈七尺，問︰得錢幾何？
術曰：以一匹尺數為法，今有布尺數乘價錢為實，實如法得錢數。
荅曰： a(=675/8)錢 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of cloth, worth 125 qian. Now there is 2 zhang and 7 chi of cloth.
Question: how much money is it worth?

The procedure says: Take the number of chi in one bolt as the divisor. Multiply the number of chi in the current cloth by the price in qian to get the dividend. Divide the dividend by the divisor to get the amount of money.

Answer: *a*(=675/8) qian.
"""

# 一匹布的尺數
匹 = 1
匹尺數 = 240  # 1 匹 = 1 丈 = 240 尺

# 一匹布的價錢
匹價錢 = 125

# 現有布的長度，2 丈 7 尺
布長度 = 2 * 240 + 7  # 1 丈 = 240 尺

# 以一匹尺數為法
法 = 匹尺數

# 今有布尺數乘價錢為實
實 = 布長度 * 匹價錢

# 實如法得錢數
a = Fraction(實, 法)  # 675/8 qian#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 675/8, Actual: 12175/48"""
