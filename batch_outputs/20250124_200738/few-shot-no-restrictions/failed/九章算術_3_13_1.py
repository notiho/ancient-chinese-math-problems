"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
術曰：以價直為法，以一匹一丈尺數乘今有錢數為實。實如法得素數。
荅曰：得素 a匹 。
"""

#----- content starts here -----
"""
Suppose there is plain silk, 1 pi (bolt) and 1 zhang in length, valued at 625 coins.
Now, there are 500 coins available.
Question: how much plain silk can be obtained?

The procedure says: Take the value as the divisor.
Multiply the length of 1 pi and 1 zhang (in chi) by the number of coins available to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of plain silk.

Answer: *a* pi of plain silk.
"""

from fractions import Fraction

# 素一匹一丈
匹 = 1
丈 = 1

# 一丈 = 10尺
尺數 = 丈 * 10

# 價直六百二十五
價直 = 625

# 今有錢五百
錢數 = 500

# 以價直為法
法 = 價直

# 以一匹一丈尺數乘今有錢數為實
實 = 匹 * 尺數 * 錢數

# 實如法得素數
a = Fraction(實, 法)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1, Actual: 8"""
