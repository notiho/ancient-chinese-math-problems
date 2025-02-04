"""
今有立木，繫索其末，委地三尺。引索卻行，去本八尺而索盡。問︰索長幾何？
術曰：以去本自乘，令如委數而一，所得，加委地數而半之，即索長
荅曰： a丈 。
"""

"""
Suppose there is a standing tree, with a rope tied to its top. The rope touches the ground at a distance of 3 chi from the base of the tree.
When pulling the rope and walking backward, the distance from the base of the tree to the person is 8 chi when the rope is fully stretched.
Question: how long is the rope?

The procedure says: Take the distance from the base (去本), square it, and divide it by the number of chi the rope touches the ground (委地數), obtaining the result.
Add the number of chi the rope touches the ground (委地數) to the result, and halve it. This gives the length of the rope.

Answer: the rope is *a* zhang long.
"""

# 委地三尺
委地數 = 3

# 去本八尺
去本 = 8

# 以去本自乘
去本平方 = 去本 * 去本

# 令如委數而一
商 = Fraction(去本平方, 委地數)

# 所得，加委地數
和 = 商 + 委地數

# 而半之，即索長
索長 = 和 / 2

# Convert to 丈 (1 丈 = 10 尺)
a = 索長 / 10
"""
"""
