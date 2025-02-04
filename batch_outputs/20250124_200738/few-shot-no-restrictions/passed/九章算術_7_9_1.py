"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
術曰：假令五日，不足五寸。令之六日，有餘一尺二寸。
荅曰： a日 。瓜長 b尺 ，瓠長 c尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 9 chi high. A melon vine grows from the top of the wall downward, growing 7 cun per day. A gourd vine grows from the bottom of the wall upward, growing 1 chi (10 cun) per day.
Question: After how many days will the two vines meet? How long will the melon vine and the gourd vine be at that time?

The procedure says: Suppose 5 days, the gap is still 5 cun. Suppose 6 days, there is an excess of 1 chi 2 cun.

Answer: *a* days. The melon vine is *b* chi long, and the gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9  # in chi

# 瓜蔓日長七寸
瓜日長 = Fraction(7, 10)  # in chi (7 cun = 7/10 chi)

# 瓠蔓日長一尺
瓠日長 = 1  # in chi

# 瓜和瓠的相對增長速度
相對增長速度 = 瓠日長 + 瓜日長  # in chi per day

# 問題：幾日相逢？
# 垣高是兩者需要共同填補的距離
a = Fraction(垣高, 相對增長速度)  # in days

# 瓜長
b = 瓜日長 * a  # in chi

# 瓠長
c = 瓠日長 * a  # in chi

# 答案
a日 = a
b尺 = b
c尺 = c

a日, b尺, c尺#----- content ends here -----

"""
"""
