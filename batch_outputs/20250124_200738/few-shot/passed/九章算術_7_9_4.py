"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
術曰：假令五日，不足五寸。令之六日，有餘一尺二寸。
荅曰： a日 。瓜長 b尺 ，瓠長 c尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 9 chi high. A melon vine grows from the top of the wall downward, extending 7 cun per day. A bottle gourd vine grows from the bottom of the wall upward, extending 1 chi per day.
Question: after how many days do they meet? How long are the melon vine and the bottle gourd vine at that time?

The procedure says: Suppose it is 5 days, it is short by 5 cun. Suppose it is 6 days, it exceeds by 1 chi and 2 cun.

Answer: *a* days. The melon vine is *b* chi long, and the bottle gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9  # chi

# 瓜蔓日長七寸
瓜蔓日長 = Fraction(7, 10)  # chi per day (7 cun = 7/10 chi)

# 瓠蔓日長一尺
瓠蔓日長 = 1  # chi per day

# 瓜、瓠蔓相對速度
相對速度 = 瓠蔓日長 + 瓜蔓日長

# 問幾何日相逢
a = Fraction(垣高, 相對速度)

# 瓜長 b尺
b = 瓜蔓日長 * a

# 瓠長 c尺
c = 瓠蔓日長 * a#----- content ends here -----

"""
"""
