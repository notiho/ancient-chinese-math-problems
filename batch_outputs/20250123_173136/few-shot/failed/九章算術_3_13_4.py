"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
術曰：以價直為法，以一匹一丈尺數乘今有錢數為實。實如法得素數。
荅曰：得素 a匹 。
"""

"""
Suppose there is plain silk, 1 pi and 1 zhang in length, worth 625 coins.
Now, there are 500 coins available. 
Question: how much plain silk can be obtained?

The procedure says: Take the value as the divisor.
Multiply the number of chi in 1 pi and 1 zhang by the number of coins available to get the dividend.
Divide the dividend by the divisor to obtain the amount of plain silk.

Answer: *a* pi of plain silk can be obtained.
"""

# 一匹一丈，價直六百二十五
價直 = 625
一匹一丈尺數 = 1 * 10  # 1 pi = 10 chi

# 今有錢五百
今有錢數 = 500

# 以一匹一丈尺數乘今有錢數為實
實 = 一匹一丈尺數 * 今有錢數

# 實如法得素數
a = Fraction(實, 價直)
"""
Variable 'a' has wrong value. Expected: 1, Actual: 8"""
