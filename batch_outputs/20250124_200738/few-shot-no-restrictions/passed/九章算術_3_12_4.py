"""
今有布一匹，價直一百二十五。今有布二丈七尺，問︰得錢幾何？
術曰：以一匹尺數為法，今有布尺數乘價錢為實，實如法得錢數。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is one bolt of cloth, valued at 125 qian. 
Now there is 2 zhang and 7 chi of cloth.
Question: how much money is it worth?

The procedure says: Take the number of chi in one bolt as the divisor.
Multiply the number of chi in the current cloth by the price of one bolt to get the dividend.
Divide the dividend by the divisor to get the amount of money.

Answer: *a* qian.
"""

# 一匹布的尺數
# 1 匹 = 4 丈 = 40 尺
一匹尺數 = 40

# 一匹布的價值
一匹價值 = 125

# 今有布二丈七尺
布尺數 = 2 * 10 + 7  # 1 丈 = 10 尺

# 以一匹尺數為法
法 = 一匹尺數

# 今有布尺數乘價錢為實
實 = 布尺數 * 一匹價值

# 實如法得錢數
a = Fraction(實, 法)

# Answer
a  # 錢#----- content ends here -----

"""
"""
