"""
今有布一匹，價直一百二十五。今有布二丈七尺，問︰得錢幾何？
術曰：以一匹尺數為法，今有布尺數乘價錢為實，實如法得錢數。
荅曰： a(=675/8)錢 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of cloth, worth 125 qian. Now there is 2 zhang and 7 chi of cloth.
Question: how much money is it worth?

The procedure says: Take the number of chi in one bolt as the divisor. Multiply the number of chi in the given cloth by the price of the bolt to get the dividend. Divide the dividend by the divisor to get the amount of money.

Answer: *a*(=675/8) qian.
"""

# 一匹布的尺數
匹 = 1  # 1 bolt of cloth
匹尺數 = 1 * 240  # 1 bolt = 240 chi (1 zhang = 10 chi, 1 bolt = 24 zhang)

# 一匹布的價錢
價錢 = 125

# 今有布二丈七尺
布丈 = 2
布尺 = 7
布尺數 = 布丈 * 10 + 布尺  # Convert to chi

# 今有布尺數乘價錢為實
實 = 布尺數 * 價錢

# 實如法得錢數
a = Fraction(實, 匹尺數)  # 675/8 qian#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 675/8, Actual: 225/16"""
