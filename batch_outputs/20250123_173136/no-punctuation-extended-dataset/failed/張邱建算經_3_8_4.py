"""
今有圓圌上周一丈五尺高一丈二尺受粟一百六十八斛五㪷二十七分㪷之五問下周幾何
術曰置粟積尺以三十六乘之以高而一所得以上周自相乘減之餘以上周尺數從而開方除之所得即下周
答曰 a丈
"""

"""
Suppose there is a circular granary with an upper circumference of 1 zhang 5 chi and a height of 1 zhang 2 chi.
It holds 168 hu, 5 dou, 27/100 dou of millet.
Question: what is the lower circumference?

The procedure says: Place the millet volume in chi, multiply it by 36, and divide by the height.
Take the result and subtract the square of the upper circumference from it.
Take the remainder, divide it by the upper circumference, and then extract the square root.
The result is the lower circumference.

Answer: *a* zhang.
"""

# 上周一丈五尺
上周 = 1 * 10 + 5  # Convert to chi (1 zhang = 10 chi)

# 高一丈二尺
高 = 1 * 10 + 2  # Convert to chi

# 粟受 168斛5斗27/100斗
粟 = 168 * 10 + 5 + Fraction(27, 100)  # Convert to dou (1 hu = 10 dou)

# 置粟積尺，以三十六乘之
積尺 = 36 * 粟

# 以高而一
積除高 = 積尺 / 高

# 所得以上周自相乘減之
減去平方 = 積除高 - 上周**2

# 餘以上周尺數從而開方
下周 = (減去平方 / 上周) ** Fraction(1, 2)

# Convert result to zhang
a = 下周 / 10  # Convert chi to zhang (1 zhang = 10 chi)
"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 1.7945863033022402"""
