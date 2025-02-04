"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
荅曰： a日 。瓜長 b尺 ，瓠長 c尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 9 chi high. A melon vine grows from the top of the wall downward, growing 7 cun per day. A gourd vine grows from the bottom of the wall upward, growing 1 chi per day.
Question: After how many days do the two vines meet? How long are the melon vine and the gourd vine at that time?

Answer: *a* days. The melon vine is *b* chi long, and the gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9  # chi

# 瓜蔓日長七寸 (convert to chi: 1 chi = 10 cun)
瓜蔓日長 = Fraction(7, 10)  # chi/day

# 瓠蔓日長一尺
瓠蔓日長 = 1  # chi/day

# Total growth per day (combined growth of both vines)
總日長 = 瓜蔓日長 + 瓠蔓日長

# Time (in days) for the vines to meet
a = Fraction(垣高, 總日長)

# Length of the melon vine (瓜) at that time
b = 瓜蔓日長 * a

# Length of the gourd vine (瓠) at that time
c = 瓠蔓日長 * a

# Final results
a, b, c#----- content ends here -----

"""
"""
