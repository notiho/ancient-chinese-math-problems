"""
今有方錐下方二丈七尺高二丈九尺問積幾何
術曰下方自乘以高乘之三而一
荅曰 a尺 
"""

#----- content starts here -----
"""
Suppose there is a square pyramid with a base side length of 2 zhang and 7 chi, and a height of 2 zhang and 9 chi.
Question: what is the volume?

The procedure says: Take the base side length, multiply it by itself, then multiply by the height.
Divide by 3 to obtain the volume.

The answer says: *a* cubic chi.
"""

# 下方二丈七尺 (convert to chi: 1 zhang = 10 chi)
下方 = 2 * 10 + 7  # Convert to chi

# 高二丈九尺 (convert to chi)
高 = 2 * 10 + 9  # Convert to chi

# 下方自乘
下方積 = 下方 * 下方

# 以高乘之
體積 = 下方積 * 高

# 三而一
a = Fraction(體積, 3)  # Volume in cubic chi#----- content ends here -----

"""
"""
