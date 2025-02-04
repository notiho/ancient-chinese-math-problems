"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
術曰：以價直為法，以一匹一丈尺數乘今有錢數為實。實如法得素數。
荅曰：得素 a(=1)匹 。
"""

#----- content starts here -----
"""
Suppose there is 1 pi of silk, measuring 1 zhang, with a value of 625 coins.
Now, with 500 coins, how much silk can be obtained?

The procedure says: Take the value as the divisor.
Take the number of chi in 1 pi and 1 zhang, and multiply it by the number of coins currently available, giving the dividend.
Divide the dividend by the divisor to obtain the amount of silk.

Answer: *a*(=1) pi of silk can be obtained.
"""

# 素一匹一丈
匹 = 1
丈 = 1

# 價直六百二十五
價直 = 625

# 今有錢五百
今有錢 = 500

# 以價直為法
法 = 價直

# 以一匹一丈尺數乘今有錢數為實
尺數 = 匹 * 丈
實 = 尺數 * 今有錢

# 實如法得素數
a = Fraction(實, 法) # 1#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1, Actual: 4/5"""
