"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
荅曰： a丈 。
"""

"""
Suppose there is a door that, when opened, moves 1 chi away from the doorframe (閫), and when closed, it does not fully meet the frame by 2 cun.
Question: how wide is the door?

Answer: the width of the door is *a* zhang.
"""

# Definitions:
# 1 zhang = 10 chi
# 1 chi = 10 cun

# 開門去閫一尺 (door moves 1 chi away from the frame)
去閫 = 1  # in chi

# 不合二寸 (door does not meet the frame by 2 cun)
不合 = Fraction(2, 10)  # convert 2 cun to chi

# The total width of the door is the sum of these two distances
a = 去閫 + 不合  # in chi

# Convert to zhang
a = Fraction(a, 10)  # convert chi to zhang

a  # The width of the door in zhang
"""
Variable 'a' has wrong value. Expected: 101/100, Actual: 3/25"""
