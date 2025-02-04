"""
今有陽馬廣五尺袤七尺高八尺問積幾何
術曰廣袤相乘以高乘之三而一
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a rectangular prism (Yangma) with a width of 5 chi, a length of 7 chi, and a height of 8 chi.
Question: what is the volume?

The procedure says: Multiply the width and the length, then multiply by the height, and divide by 3.

Answer: *a* chi³.
"""

# 陽馬廣五尺
廣 = 5

# 袤七尺
袤 = 7

# 高八尺
高 = 8

# 廣袤相乘
底面積 = 廣 * 袤

# 以高乘之
體積 = 底面積 * 高

# 三而一
a = Fraction(體積, 3)#----- content ends here -----

"""
"""
