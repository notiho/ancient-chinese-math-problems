"""
今有布一匹價直一百二十五今有布二丈七尺問得錢幾何
術曰以一匹尺數為法今有布尺數乘價錢為實實如法得錢數
荅曰 a錢 
"""

#----- content starts here -----
"""
Suppose there is a bolt of cloth (1 pi) worth 125 qian. Now there is a piece of cloth measuring 2 zhang and 7 chi.
Question: how much money is it worth?

The procedure says: Take the number of chi in one bolt of cloth as the divisor.
Take the number of chi in the given piece of cloth and multiply it by the price in qian, obtaining the dividend.
Divide the dividend by the divisor to obtain the amount of money.

The answer says: *a* qian.
"""

# 一匹布的尺數 (1 匹 = 1 丈 = 10 尺)
一匹尺數 = 10

# 一匹布的價值
匹價 = 125

# 現有布的長度 (2 丈 7 尺 = 2*10 + 7 尺)
布尺數 = 2 * 10 + 7

# 以一匹尺數為法
法 = 一匹尺數

# 現有布尺數乘價錢為實
實 = 布尺數 * 匹價

# 實如法得錢數
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 675/8, Actual: 675/2"""
