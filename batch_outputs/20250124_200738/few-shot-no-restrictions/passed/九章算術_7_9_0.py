"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
術曰：假令五日，不足五寸。令之六日，有餘一尺二寸。
荅曰： a日 。瓜長 b尺 ，瓠長 c尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 9 chi high. A melon vine grows from the top of the wall downward, growing 7 cun per day. A bottle gourd vine grows from the bottom of the wall upward, growing 1 chi per day.
Question: after how many days do the two vines meet? How long are the melon vine and the bottle gourd vine at that time?

The procedure says: Assume 5 days, but it is 5 cun short. Assume 6 days, and it exceeds by 1 chi 2 cun.

Answer: *a* days. The melon vine is *b* chi long, and the bottle gourd vine is *c* chi long.
"""

from fractions import Fraction

# 垣高九尺
垣高 = 9  # chi

# 瓜蔓日長七寸
瓜日長 = Fraction(7, 10)  # chi per day (convert 7 cun to chi)

# 瓠蔓日長一尺
瓠日長 = 1  # chi per day

# 瓜和瓠的相對增長速度
相對增長速度 = 瓠日長 + 瓜日長  # chi per day

# 問：幾何日相逢？
# 總距離是垣高，時間 = 距離 / 相對增長速度
a = Fraction(垣高, 相對增長速度)  # days

# 瓜長 b 尺
b = 瓜日長 * a  # chi

# 瓠長 c 尺
c = 瓠日長 * a  # chi

# Final results
a日 = a
b尺 = b
c尺 = c

a日, b尺, c尺#----- content ends here -----

"""
"""
