"""
今有方錐下方二丈七尺，高二丈九尺。問︰積幾何？
術曰：下方自乘，以高乘之，三而一。
荅曰： a(=7047)尺 。
"""

#----- content starts here -----
"""
Suppose there is a square pyramid with a base side length of 2 zhang and 7 chi, and a height of 2 zhang and 9 chi.
Question: what is the volume?

The procedure says: Multiply the base side length by itself. Multiply the result by the height. Divide by 3.

Answer: *a*(=7047) chi³.
"""

# 下方二丈七尺
下方 = 2 * 10 + 7  # Convert to chi (1 zhang = 10 chi)

# 高二丈九尺
高 = 2 * 10 + 9  # Convert to chi (1 zhang = 10 chi)

# 下方自乘
下方積 = 下方 * 下方

# 以高乘之
體積 = 下方積 * 高

# 三而一
a = Fraction(體積, 3)  # 7047 chi³#----- content ends here -----

"""
"""
