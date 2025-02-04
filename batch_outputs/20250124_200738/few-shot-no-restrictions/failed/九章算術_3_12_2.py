"""
今有布一匹，價直一百二十五。今有布二丈七尺，問︰得錢幾何？
術曰：以一匹尺數為法，今有布尺數乘價錢為實，實如法得錢數。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of cloth, worth 125 qian. 
Now there is 2 zhang and 7 chi of cloth.
Question: how much money is it worth?

The procedure says: Take the number of chi in one bolt as the divisor.
Multiply the number of chi in the given cloth by the price of one bolt to get the dividend.
Divide the dividend by the divisor to get the amount of money.

Answer: *a* qian.
"""

# 一匹布的尺數
匹長 = 1  # 1 匹 = 1 丈 = 10 尺

# 一匹布的價值
匹價 = 125  # 錢

# 現有布的長度：2 丈 7 尺
布長 = 2 * 10 + 7  # 2 丈 = 20 尺，加上 7 尺

# 以一匹尺數為法
法 = 匹長 * 10  # 1 匹 = 10 尺

# 今有布尺數乘價錢為實
實 = 布長 * 匹價

# 實如法得錢數
a = Fraction(實, 法)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 675/8, Actual: 675/2"""
