"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
術曰：以去本自乘，令如委數而一，所得，加委地數而半之，即索長
荅曰： a(=73/60)丈 。
"""

#----- content starts here -----
"""
Suppose there is a standing tree, with a rope tied to its top. The rope touches the ground at a distance of 3 chi from the base of the tree.
Pulling the rope backward, one walks 8 chi away from the base of the tree until the rope is fully stretched.
Question: how long is the rope?

The procedure says: Take the distance from the base (去本) and square it. Divide it by the distance where the rope touches the ground (委地數), treating it as 1.
Add the result to the distance where the rope touches the ground (委地數), then halve the sum. This gives the length of the rope.

Answer: *a*(=73/60) zhang.
"""

# 委地數 (distance where the rope touches the ground)
委地數 = 3  # chi

# 去本 (distance walked away from the base)
去本 = 8  # chi

# 以去本自乘
去本平方 = 去本 * 去本

# 令如委數而一
商 = Fraction(去本平方, 委地數)

# 所得，加委地數
和 = 商 + 委地數

# 而半之，即索長
索長 = Fraction(和, 2)

# Convert chi to zhang (1 zhang = 10 chi)
a = Fraction(索長, 10)  # 73/60 zhang#----- content ends here -----

"""
"""
