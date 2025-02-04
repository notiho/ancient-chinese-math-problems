"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
術曰：以去本自乘，令如委數而一，所得，加委地數而半之，即索長
荅曰： a(=73/60)丈 。
"""

#----- content starts here -----
"""
Suppose there is a standing tree, with a rope tied to its top. The rope touches the ground at a distance of 3 chi from the base of the tree.
If the rope is pulled taut and one walks backward, moving 8 chi away from the base of the tree, the rope becomes fully extended.
Question: how long is the rope?

The procedure says: Take the distance from the base (去本) and square it. Divide it by the number of chi the rope touches the ground (委地數), treating it as the divisor. Add the result to the number of chi the rope touches the ground (委地數), then halve it. This gives the length of the rope.

Answer: *a*(=73/60) zhang.
"""

# 委地三尺
委地 = 3

# 去本八尺
去本 = 8

# 以去本自乘
去本自乘 = 去本 * 去本

# 令如委數而一 (divide by 委地數)
商 = Fraction(去本自乘, 委地)

# 所得，加委地數
和 = 商 + 委地

# 而半之，即索長
索長 = Fraction(和, 2)

# Convert to 丈 (1 丈 = 10 尺)
a = Fraction(索長, 10)  # 73/60 丈#----- content ends here -----

"""
"""
