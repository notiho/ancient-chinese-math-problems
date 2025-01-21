"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
術曰：假令五日，不足五寸。令之六日，有餘一尺二寸。
荅曰： a日 。瓜長 b尺 ，瓠長 c尺 。
"""

"""
Suppose there is a wall 9 chi high. A melon vine grows upward from the top of the wall, extending 7 cun per day.
A gourd vine grows upward from the bottom of the wall, extending 1 chi per day.
Question: after how many days do they meet? How long are the melon vine and gourd vine respectively?

The procedure says: Suppose it is 5 days, the difference is less than 5 cun.
Suppose it is 6 days, the difference is 1 chi 2 cun more.

Answer: *a* days. The melon vine is *b* chi long, and the gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9  # chi

# 瓜蔓日長七寸
瓜日長 = Fraction(7, 10)  # chi per day (convert 7 cun to chi)

# 瓠蔓日長一尺
瓠日長 = 1  # chi per day

# 瓜、瓠相對日長
相對日長 = 瓠日長 + 瓜日長

# 問幾日相逢
a = Fraction(垣高, 相對日長)

# 瓜長
b = 瓜日長 * a

# 瓠長
c = 瓠日長 * a
"""
"""
