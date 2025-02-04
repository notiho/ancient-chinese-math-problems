"""
今有倉東西袤一丈四尺南北廣八尺南壁高一丈受粟六百二十二斛九分斛之二問北壁高幾何
術曰置粟積尺以倉廣袤相乘而一所得倍之減南壁高尺數餘為北壁高
答曰 a尺
"""

"""
Suppose there is a granary with an east-west length of 1 zhang 4 chi, a north-south width of 8 chi, and a south wall height of 1 zhang. 
It holds 622 hu and 2/9 of a hu of grain. 
Question: how high is the north wall?

The procedure says: Place the grain volume in cubic chi. 
Multiply the granary's width and length together, and take the result as 1 unit. 
Double this result, subtract the height of the south wall in chi, and the remainder is the height of the north wall.

Answer: the north wall is *a* chi.
"""

# 倉東西袤一丈四尺
東西袤 = 1 * 10 + 4  # Convert to chi (1 zhang = 10 chi)

# 南北廣八尺
南北廣 = 8  # chi

# 南壁高一丈
南壁高 = 1 * 10  # Convert to chi

# 受粟六百二十二斛九分斛之二
粟積 = 622 + Fraction(2, 9)  # Convert to hu
粟積尺 = 粟積 * 100  # Convert hu to cubic chi (1 hu = 100 cubic chi)

# 以倉廣袤相乘
廣袤積 = 東西袤 * 南北廣

# 所得倍之
倍積 = 2 * 廣袤積

# 減南壁高尺數
北壁高 = Fraction(粟積尺, 倍積) - 南壁高

# 餘為北壁高
a = 北壁高

"""
Variable 'a' has wrong value. Expected: 8, Actual: 2410/9"""
