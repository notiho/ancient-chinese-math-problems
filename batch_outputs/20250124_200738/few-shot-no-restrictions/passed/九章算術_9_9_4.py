"""
今有開門去閫一尺，不合二寸。問︰門廣幾何？
術曰：以去閫一尺自乘，所得，以不合二寸半之而一，所得，增不合之半，即得門廣。
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a door that is 1 chi away from the threshold and does not close by 2 cun.
Question: how wide is the door?

The procedure says: Take the distance from the threshold (1 chi) and square it. 
Divide the result by the amount it does not close (2 cun), halved. 
Add half of the amount it does not close to the result. 
This gives the width of the door.

Answer: the width of the door is *a* zhang.
"""

from fractions import Fraction

# 去閫一尺 (distance from the threshold)
去閫 = 1  # in chi

# 不合二寸 (does not close by 2 cun)
不合 = Fraction(2, 10)  # 2 cun = 2/10 chi

# Step 1: Square the distance from the threshold
step1 = 去閫 ** 2

# Step 2: Divide by half of the amount it does not close
step2 = step1 / (不合 / 2)

# Step 3: Add half of the amount it does not close
門廣 = step2 + (不合 / 2)

# Convert to zhang (1 zhang = 10 chi)
a = 門廣 / 10  # Convert chi to zhang

a#----- content ends here -----

"""
"""
