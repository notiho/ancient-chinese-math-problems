"""
今有布一匹價直一百二十五今有布二丈七尺問得錢幾何
術曰以一匹尺數為法今有布尺數乘價錢為實實如法得錢數
荅曰 a錢 
"""

#----- content starts here -----
"""
Suppose there is one bolt of cloth worth 125 qian. Now there is 2 zhang and 7 chi of cloth.
Question: how much money is it worth?

The procedure says: Take the number of chi in one bolt as the divisor.
Now, take the number of chi in the given cloth and multiply it by the price in qian, obtaining the dividend.
Divide the dividend by the divisor to get the amount of money.

The answer says: *a* qian.
"""

# 一匹布的尺數 (1 匹 = 4 丈)
一匹布尺數 = 4 * 10  # 1 丈 = 10 尺

# 一匹布的價值
一匹布價值 = 125

# 現有布的長度 (2 丈 7 尺)
現有布尺數 = 2 * 10 + 7  # 2 丈 = 20 尺，加上 7 尺

# 以一匹尺數為法
法 = 一匹布尺數

# 現有布尺數乘價錢為實
實 = 現有布尺數 * 一匹布價值

# 實如法得錢數
a = Fraction(實, 法)  # 結果以分數表示
#----- content ends here -----

"""
"""
