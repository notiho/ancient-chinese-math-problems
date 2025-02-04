"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
術曰：以去本自乘，令如委數而一，所得，加委地數而半之，即索長
荅曰： a(=73/60)丈 。
"""

#----- content starts here -----
"""
Suppose there is a standing tree, and a rope is tied to its top. The rope touches the ground 3 chi away from the base of the tree.
Pulling the rope backward, one moves 8 chi away from the base of the tree, and the rope is fully stretched.
Question: how long is the rope?

The procedure says: Multiply the distance from the base by itself. Divide it by the distance the rope touches the ground (3 chi), obtaining a result. Add the distance the rope touches the ground (3 chi) to this result, and halve it. This gives the length of the rope.

Answer: *a*(=73/60) zhang.
"""

# 委地三尺
委地 = 3

# 去本八尺
去本 = 8

# 以去本自乘
去本平方 = 去本 * 去本

# 令如委數而一
商 = Fraction(去本平方, 委地)

# 所得，加委地數
和 = 商 + 委地

# 而半之，即索長
索長 = Fraction(和, 2)

# Convert to 丈 (1 丈 = 10 尺)
a = Fraction(索長, 10) # 73/60 丈#----- content ends here -----

"""
"""
