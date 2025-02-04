"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
術曰：以價直為法，以一匹一丈尺數乘今有錢數為實。實如法得素數。
荅曰：得素 a匹 。
"""

#----- content starts here -----
"""
Suppose there is plain silk, 1 pi (bolt) and 1 zhang in length, with a value of 625 coins.
Now, there are 500 coins available.
Question: how much plain silk can be obtained?

The procedure says: Take the value (625) as the divisor.
Multiply the length of 1 pi and 1 zhang (in chi) by the available coins (500) to get the dividend.
Divide the dividend by the divisor to obtain the amount of plain silk.

Answer: *a* pi.
"""

from fractions import Fraction

# 1匹1丈 (1 pi and 1 zhang)
# 1丈 = 10尺
匹長度 = 10  # in chi

# 價直六百二十五
價直 = 625  # coins

# 今有錢五百
今有錢 = 500  # coins

# 以一匹一丈尺數乘今有錢數為實
實 = 匹長度 * 今有錢

# 實如法得素數
a = Fraction(實, 價直)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1, Actual: 8"""
