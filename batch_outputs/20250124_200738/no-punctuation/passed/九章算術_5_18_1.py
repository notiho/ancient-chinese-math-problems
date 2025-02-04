"""
今有塹堵下廣二丈袤一十八丈六尺高二丈五尺問積幾何
術曰廣袤相乘以高乘之二而一
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a trench wall with a bottom width of 2 zhang, a length of 18 zhang 6 chi, and a height of 2 zhang 5 chi.
Question: what is the volume?

The procedure says: Multiply the width and the length, then multiply by the height, and divide by 2.

The answer says: *a* chi³.
"""

# 下廣二丈
廣 = 2 * 10  # Convert zhang to chi

# 袤一十八丈六尺
袤 = 18 * 10 + 6  # Convert zhang to chi and add chi

# 高二丈五尺
高 = 2 * 10 + 5  # Convert zhang to chi and add chi

# 廣袤相乘
底面積 = 廣 * 袤

# 以高乘之
體積 = 底面積 * 高

# 二而一
a = Fraction(體積, 2)  # Divide by 2 to get the final volume in chi³#----- content ends here -----

"""
"""
