"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
術曰：假令五日，不足五寸。令之六日，有餘一尺二寸。
荅曰： a(=90/17)日 。瓜長 b(=63/17)尺 ，瓠長 c(=90/17)尺 。
"""

"""
Suppose there is a wall 9 chi high. A melon grows on top of it, and its vine grows upward at a rate of 7 cun per day.
A gourd grows at the bottom of the wall, and its vine grows upward at a rate of 1 chi per day.
Question: after how many days will the two vines meet? How long will the melon vine and the gourd vine be at that time?

The procedure says: Suppose it is 5 days, and the difference is less than 5 cun.
Suppose it is 6 days, and the difference is more than 1 chi 2 cun.

Answer: *a*(=90/17) days. The melon vine is *b*(=63/17) chi long, and the gourd vine is *c*(=90/17) chi long.
"""

# 垣高九尺
垣高 = 9

# 瓜蔓日長七寸
瓜蔓日長 = Fraction(7, 10)  # Convert 7 cun to chi (1 chi = 10 cun)

# 瓠蔓日長一尺
瓠蔓日長 = 1

# 瓜蔓與瓠蔓日長之和
蔓日長和 = 瓜蔓日長 + 瓠蔓日長

# 問幾何日相逢
a = Fraction(垣高, 蔓日長和)  # 90/17 days

# 瓜長
b = 瓜蔓日長 * a  # 63/17 chi

# 瓠長
c = 瓠蔓日長 * a  # 90/17 chi
"""
"""
