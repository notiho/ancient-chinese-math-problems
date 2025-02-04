"""
今有方亭下方五丈上方四丈高五丈問積幾何
術曰上下方相乘又各自乘并之以高乘之三而一
荅曰 a尺 
"""

"""
Suppose there is a square pavilion with a bottom square side of 5 zhang, a top square side of 4 zhang, and a height of 5 zhang.
Question: what is the volume?

The procedure says: Multiply the bottom square side by the top square side.
Then, multiply each square side by itself and add these together.
Multiply the result by the height.
Divide by 3 to obtain the volume.

Answer: *a* chi³.
"""

# 下方五丈
下方 = 5

# 上方四丈
上方 = 4

# 高五丈
高 = 5

# 上下方相乘
上下相乘 = 下方 * 上方

# 又各自乘并之
各自平方和 = 下方**2 + 上方**2

# 并之以高乘之
體積未除 = (上下相乘 + 各自平方和) * 高

# 三而一
a = Fraction(體積未除, 3) * 1000  # Convert from zhang³ to chi³ (1 zhang³ = 1000 chi³)
"""
"""
