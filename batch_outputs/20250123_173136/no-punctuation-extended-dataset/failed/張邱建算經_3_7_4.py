"""
今有倉東西袤一丈四尺南北廣八尺南壁高一丈受粟六百二十二斛九分斛之二問北壁高幾何
術曰置粟積尺以倉廣袤相乘而一所得倍之減南壁高尺數餘為北壁高
答曰 a尺
"""

"""
Suppose there is a granary with an east-west length of 1 zhang 4 chi, a north-south width of 8 chi, and a south wall height of 1 zhang.
It holds 622 hu and 2/9 of a hu of grain.
Question: how high is the north wall?

The procedure says: Place the total grain volume in cubic chi.
Multiply the granary's width and length together, and take the result as 1 unit.
Double this result, subtract the height of the south wall in chi, and the remainder is the height of the north wall.

Answer: *a* chi.
"""

# 倉東西袤一丈四尺
袤 = 1 * 10 + 4  # Convert zhang to chi

# 南北廣八尺
廣 = 8

# 南壁高一丈
南壁高 = 1 * 10  # Convert zhang to chi

# 受粟六百二十二斛九分斛之二
粟 = 622 + Fraction(2, 9)  # Convert hu to fractional form

# 1斛 = 10立方尺
粟積尺 = 10 * 粟  # Convert hu to cubic chi

# 以倉廣袤相乘
基面積 = 廣 * 袤  # Base area of the granary in square chi

# 而一所得倍之
倍基面積 = 2 * 基面積

# 減南壁高尺數
北壁高 = Fraction(粟積尺, 倍基面積) - 南壁高

# 餘為北壁高
a = 北壁高
"""
Variable 'a' has wrong value. Expected: 8, Actual: 160/9"""
