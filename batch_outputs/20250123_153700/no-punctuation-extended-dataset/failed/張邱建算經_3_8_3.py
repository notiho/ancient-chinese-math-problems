"""
今有圓圌上周一丈五尺高一丈二尺受粟一百六十八斛五㪷二十七分㪷之五問下周幾何
術曰置粟積尺以三十六乘之以高而一所得以上周自相乘減之餘以上周尺數從而開方除之所得即下周
答曰 a丈
"""

"""
Suppose there is a circular granary with an upper circumference of 1 zhang 5 chi and a height of 1 zhang 2 chi. It holds 168 hu, 5 dou, 27/5 dou of millet.
Question: what is the lower circumference?

The procedure says: Place the millet volume in chi, multiply it by 36, and divide by the height.
From the result, subtract the square of the upper circumference.
Take the remainder, divide by the upper circumference, and then extract the square root.
The result is the lower circumference.

Answer: *a* zhang.
"""

from fractions import Fraction

# 上周一丈五尺
上周 = 1 * 10 + 5  # Convert to chi (1 zhang = 10 chi)

# 高一丈二尺
高 = 1 * 10 + 2  # Convert to chi

# 粟受量：168斛5斗27分斗之5
粟 = 168 * 10 + 5 + Fraction(27, 5)  # Convert to dou (1 hu = 10 dou)

# 術曰置粟積尺，以三十六乘之
積尺 = 粟 * 36

# 以高而一
積尺 = 積尺 / 高

# 所得以上周自相乘減之
減之 = 積尺 - 上周**2

# 餘以上周尺數從而開方除之
下周 = (減之 / 上周)**0.5

# Convert result to zhang
a = 下周 / 10  # Convert chi back to zhang
"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 1.7974426277353053"""
