"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a door that, when opened, moves 1 chi away from the doorframe (閫) and does not close by 2 cun.
Question: how wide is the door?

Answer: the door is *a* zhang wide.
"""

# 開門去閫一尺 (1 chi = 10 cun)
去閫 = 10  # in cun

# 不合二寸
不合 = 2  # in cun

# The total width of the door is the sum of the distance moved away and the gap left
門廣 = 去閫 + 不合

# Convert the width into zhang (1 zhang = 100 cun)
a = Fraction(門廣, 100)  # in zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 101/100, Actual: 3/25"""
