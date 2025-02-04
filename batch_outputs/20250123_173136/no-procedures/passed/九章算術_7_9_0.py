"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
荅曰： a日 。瓜長 b尺 ，瓠長 c尺 。
"""

"""
Suppose there is a wall 9 chi high. A melon vine grows from the top of the wall downward, extending 7 cun per day. A gourd vine grows from the bottom of the wall upward, extending 1 chi per day.
Question: after how many days do they meet? How long are the melon vine and the gourd vine respectively?

Answer: *a* days. The melon vine is *b* chi long, and the gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9  # chi

# 瓜蔓日長七寸 (convert to chi: 1 chi = 10 cun)
瓜蔓日長 = Fraction(7, 10)  # chi per day

# 瓠蔓日長一尺
瓠蔓日長 = 1  # chi per day

# Total growth per day (combined)
總蔓日長 = 瓜蔓日長 + 瓠蔓日長

# Days until they meet
a = Fraction(垣高, 總蔓日長)

# Length of the melon vine (瓜) after a days
b = 瓜蔓日長 * a

# Length of the gourd vine (瓠) after a days
c = 瓠蔓日長 * a

# Results
a, b, c
"""
"""
