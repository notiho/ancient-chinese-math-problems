"""
今有圓圌上周一丈五尺高一丈二尺受粟一百六十八斛五㪷二十七分㪷之五問下周幾何
術曰置粟積尺以三十六乘之以高而一所得以上周自相乘減之餘以上周尺數從而開方除之所得即下周
答曰 a丈
"""

"""
Suppose there is a circular granary with an upper circumference of 1 zhang 5 chi, a height of 1 zhang 2 chi, and it holds 168 hu, 5 dou, and 27/30 dou of millet.
Question: what is the lower circumference?

The procedure says: Place the millet volume in cubic chi, multiply it by 36, and divide by the height.
Take the result and subtract the square of the upper circumference.
The remainder is divided by the upper circumference in chi, and the square root of the result is taken.
This gives the lower circumference.

Answer: *a* zhang.
"""

# 上周一丈五尺
上周 = 1 * 10 + 5  # Convert to chi

# 高一丈二尺
高 = 1 * 10 + 2  # Convert to chi

# 粟一百六十八斛五斗二十七分斗之五
粟 = 168 * 10 + 5 + Fraction(27, 30)  # Convert to dou
粟積尺 = 粟 * 10  # Convert dou to cubic chi

# 置粟積尺，以三十六乘之
積 = 粟積尺 * 36

# 以高而一
積除高 = Fraction(積, 高)

# 所得以上周自相乘減之
減項 = 上周 ** 2
餘 = 積除高 - 減項

# 餘以上周尺數從而開方除之
下周 = Fraction(餘, 上周) ** Fraction(1, 2)

# Convert to zhang
a = Fraction(下周, 10)  # Convert chi to zhang
"""
Code error: both arguments should be Rational instances"""
