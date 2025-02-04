"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
術曰：以去本自乘，令如委數而一，所得，加委地數而半之，即索長
荅曰： a丈 。
"""

"""
Suppose there is an upright tree, with a rope tied to its top. The rope touches the ground at a distance of 3 chi from the base of the tree.
When pulling the rope and walking backward, the person is 8 chi away from the base of the tree when the rope is fully stretched.
Question: how long is the rope?

The procedure says: Take the distance from the base (去本) and square it. Divide it by the distance where the rope touches the ground (委地數), obtaining a result.
Add this result to the distance where the rope touches the ground (委地數), and halve it. This gives the length of the rope.

The answer says: *a* zhang.
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

# Convert 索長 from chi to zhang (1 zhang = 10 chi)
a = Fraction(索長, 10)
"""
"""
