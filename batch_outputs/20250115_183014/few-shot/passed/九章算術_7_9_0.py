"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
術曰：假令五日，不足五寸。令之六日，有餘一尺二寸。
荅曰： a日 。瓜長 b尺 ，瓠長 c尺 。
"""

"""
Suppose there is a wall 9 chi high. A melon vine grows upward from the top of the wall, extending 7 cun per day. A gourd vine grows upward from the bottom of the wall, extending 1 chi per day.
Question: after how many days do they meet? How long are the melon vine and the gourd vine respectively?

The procedure says: Suppose it is 5 days, then the difference is less than 5 cun. Suppose it is 6 days, then the difference exceeds 1 chi 2 cun.

Answer: *a* days. The melon vine is *b* chi long, and the gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9

# 瓜蔓日長七寸
瓜蔓日長 = Fraction(7, 10)  # Convert 7 cun to chi (1 chi = 10 cun)

# 瓠蔓日長一尺
瓠蔓日長 = 1

# 瓜、瓠蔓日長之和
蔓日長和 = 瓜蔓日長 + 瓠蔓日長

# 幾何日相逢？
# 瓜蔓和瓠蔓的增長速度之和每天縮短垣高
a = Fraction(垣高, 蔓日長和)

# 瓜長幾何？
b = 瓜蔓日長 * a

# 瓠長幾何？
c = 瓠蔓日長 * a

# 答案
a日 = a
b尺 = b
c尺 = c
"""
"""
