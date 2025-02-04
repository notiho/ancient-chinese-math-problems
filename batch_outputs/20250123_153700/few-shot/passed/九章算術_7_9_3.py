"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
術曰：假令五日，不足五寸。令之六日，有餘一尺二寸。
荅曰： a日 。瓜長 b尺 ，瓠長 c尺 。
"""

"""
Suppose there is a wall 9 chi high. A melon vine grows upward from the top of the wall, extending 7 cun per day.
A gourd vine grows upward from the bottom of the wall, extending 1 chi per day.
Question: after how many days do they meet? How long are the melon vine and gourd vine respectively?

The procedure says: Suppose it is 5 days, and the difference is less than 5 cun.
Suppose it is 6 days, and the difference exceeds 1 chi 2 cun.

Answer: *a* days. The melon vine is *b* chi long, and the gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9  # chi

# 瓜蔓日長七寸
瓜日長 = Fraction(7, 10)  # chi per day (convert 7 cun to chi)

# 瓠蔓日長一尺
瓠日長 = 1  # chi per day

# 瓜、瓠相向而行，求相逢日
# Let days = a
# Total growth of melon vine = 瓜日長 * a
# Total growth of gourd vine = 瓠日長 * a
# Combined growth = 瓜日長 * a + 瓠日長 * a
# They meet when combined growth equals 垣高

a = 垣高 / (瓜日長 + 瓠日長)

# 瓜長 b尺
b = 瓜日長 * a

# 瓠長 c尺
c = 瓠日長 * a

a, b, c
"""
"""
