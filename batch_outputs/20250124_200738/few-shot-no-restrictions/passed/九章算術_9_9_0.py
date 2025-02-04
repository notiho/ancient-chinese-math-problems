"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a door, with the distance to the threshold being 1 chi, and the gap when the door is closed being 2 cun.
Question: how wide is the door?

The procedure says: Take the distance to the threshold (1 chi) and square it. 
Divide the result by the gap (2 cun), halved, and then add half of the gap to the result.
This gives the width of the door.

Answer: the door is *a* zhang wide.
"""

from fractions import Fraction

# 去閫一尺 (distance to the threshold)
去閫 = 1  # in chi

# 不合二寸 (gap when the door is closed)
不合 = Fraction(2, 10)  # 2 cun = 2/10 chi

# Step 1: Square the distance to the threshold
step1 = 去閫 ** 2

# Step 2: Divide the result by half of the gap
step2 = step1 / (不合 / 2)

# Step 3: Add half of the gap to the result
門廣 = step2 + (不合 / 2)

# Convert the result to zhang (1 zhang = 10 chi)
a = 門廣 / 10  # in zhang

a#----- content ends here -----

"""
"""
