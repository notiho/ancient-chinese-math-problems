"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
術曰：以去本自乘，令如委數而一，所得，加委地數而半之，即索長
荅曰： a丈 。
"""

"""
Suppose there is a standing tree, with a rope tied to its top. The rope touches the ground at a distance of 3 chi from the base of the tree.
When the rope is pulled taut and walked away, the person is 8 chi from the base of the tree when the rope is fully extended.
Question: how long is the rope?

The procedure says: Square the distance from the base (去本自乘). Divide it by the ground distance (委數), obtaining a result. Add the ground distance (委地數) to the result, and take half of it. This is the length of the rope.

Answer: the rope is *a* zhang.
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
索長 = 和 / 2

# Convert 索長 to 丈 (1 丈 = 10 尺)
a = 索長 / 10
"""
"""
