"""
今有圓圌上周一丈五尺高一丈二尺受粟一百六十八斛五㪷二十七分㪷之五問下周幾何
術曰置粟積尺以三十六乘之以高而一所得以上周自相乘減之餘以上周尺數從而開方除之所得即下周
答曰 a丈
"""

#----- content starts here -----
"""
Suppose there is a circular granary with an upper circumference of 1 zhang 5 chi, a height of 1 zhang 2 chi, and it holds 168 hu, 5 dou, and 27/30 dou of millet.
Question: what is the lower circumference?

The procedure says: Place the millet volume in cubic chi. Multiply it by 36. Divide it by the height.
Take the result and subtract the square of the upper circumference.
Take the remainder, divide it by the upper circumference, and then extract the square root. 
The result is the lower circumference.

Answer: *a* zhang.
"""

# 上周一丈五尺
上周 = 1 * 10 + 5  # Convert to chi

# 高一丈二尺
高 = 1 * 10 + 2  # Convert to chi

# 粟一百六十八斛五㪷二十七分㪷之五
粟 = 168 * 10 + 5 + Fraction(27, 30)  # Convert to dou

# 置粟積尺，以三十六乘之
粟積尺 = 粟 * 36

# 以高而一
積高 = 粟積尺 / 高

# 所得以上周自相乘減之
減值 = 積高 - 上周**2

# 餘以上周尺數從而開方
下周 = (減值 / 上周)**0.5

# 答案以丈為單位
a = 下周 / 10  # Convert chi to zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9/5, Actual: 1.794937324811092"""
