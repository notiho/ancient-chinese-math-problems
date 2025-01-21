"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
荅曰： a丈 。
"""

"""
Suppose there is a tree 2 zhang tall, with a circumference of 3 chi. A vine grows from the base of the tree, wrapping around the tree 7 times and reaching the top of the tree.  
Question: How long is the vine?

Answer: The vine is *a* zhang long.
"""

# 木長二丈
木高 = 2  # in zhang

# 圍之三尺
木圍 = 3  # in chi
木圍 = Fraction(3, 10)  # convert chi to zhang (10 chi = 1 zhang)

# 葛纏木七周
纏繞次數 = 7

# The vine forms a helical path. Its length is the hypotenuse of a right triangle where:
# - the height of the tree is the vertical side
# - the total horizontal distance (circumference * number of wraps) is the horizontal side
垂直距離 = 木高
水平距離 = 木圍 * 纏繞次數

# Use the Pythagorean theorem to calculate the vine's length
葛長 = (垂直距離**2 + 水平距離**2)**0.5

# 葛長 in zhang
a = 葛長

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 29/10, Actual: 2.9"""
