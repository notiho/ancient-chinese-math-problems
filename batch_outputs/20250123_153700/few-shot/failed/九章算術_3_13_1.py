"""
今有素一匹一丈，價直六百二十五。今有錢五百，問︰得素幾何？
術曰：以價直為法，以一匹一丈尺數乘今有錢數為實。實如法得素數。
荅曰：得素 a匹 。
"""

"""
Suppose there is plain silk, 1 pi (bolt) and 1 zhang in length, worth 625 coins.
Now, there are 500 coins available.
Question: how much plain silk can be obtained?

The procedure says: Take the price as the divisor.
Take the number of chi in 1 pi and 1 zhang, and multiply it by the number of coins available, giving the dividend.
Divide the dividend by the divisor to obtain the amount of plain silk.

Answer: *a* pi (bolt) of plain silk can be obtained.
"""

# 一匹一丈
匹 = 1  # 1 pi
丈 = 1  # 1 zhang = 10 chi
尺數 = 匹 * 10 + 丈 * 10  # Convert to chi (1 pi = 10 chi, 1 zhang = 10 chi)

# 價直六百二十五
價直 = 625

# 今有錢五百
今有錢 = 500

# 以一匹一丈尺數乘今有錢數為實
實 = 尺數 * 今有錢

# 實如法得素數
a = Fraction(實, 價直)  # Result in pi (bolt)
"""
Variable 'a' has wrong value. Expected: 1, Actual: 16"""
