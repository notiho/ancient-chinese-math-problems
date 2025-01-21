"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
荅曰： a日 。瓜長 b尺 ，瓠長 c尺 。
"""

"""
Suppose there is a wall 9 chi high. A melon vine grows from the top of the wall downward, increasing by 7 cun per day. A gourd vine grows from the bottom of the wall upward, increasing by 1 chi per day.
Question: After how many days do they meet? How long are the melon vine and the gourd vine at that time?

Answer: They meet after *a* days. The melon vine is *b* chi long, and the gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9  # chi

# 瓜蔓日長七寸 (convert to chi: 1 chi = 10 cun)
瓜蔓日長 = Fraction(7, 10)  # chi per day

# 瓠蔓日長一尺
瓠蔓日長 = 1  # chi per day

# Let the number of days be a
# The total distance covered by both vines in a day is 瓜蔓日長 + 瓠蔓日長
每日合計長度 = 瓜蔓日長 + 瓠蔓日長

# The vines meet when their combined growth equals the height of the wall
a = Fraction(垣高, 每日合計長度)

# The length of the melon vine (瓜) is its daily growth multiplied by the number of days
b = 瓜蔓日長 * a

# The length of the gourd vine (瓠) is its daily growth multiplied by the number of days
c = 瓠蔓日長 * a

# Results
a, b, c
"""
"""
