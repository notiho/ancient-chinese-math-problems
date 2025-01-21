"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
術曰：以價直為法，以一匹一丈尺數乘今有錢數為實。實如法得素數。
荅曰：得素 a匹 。
"""

"""
Suppose there is plain silk, 1 pi and 1 zhang in length, valued at 625 coins.
Now, with 500 coins, how much silk can be obtained?

The procedure says: Take the value as the divisor.
Multiply the length of 1 pi and 1 zhang (in chi) by the number of coins currently available, giving the dividend.
Divide the dividend by the divisor to obtain the amount of silk.

Answer: *a* pi of silk can be obtained.
"""

# 一匹一丈 (1 pi = 10 zhang, 1 zhang = 10 chi)
一匹一丈尺數 = 10 * 10  # Convert to chi

# 價直六百二十五
價直 = 625

# 今有錢五百
今有錢數 = 500

# 以一匹一丈尺數乘今有錢數為實
實 = 一匹一丈尺數 * 今有錢數

# 實如法得素數
a = Fraction(實, 價直) / 一匹一丈尺數
"""
Variable 'a' has wrong value. Expected: 1, Actual: 4/5"""
