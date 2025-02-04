"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
術曰：假令五日，不足五寸。令之六日，有餘一尺二寸。
荅曰： a(=90/17)日 。瓜長 b(=63/17)尺 ，瓠長 c(=90/17)尺 。
"""

"""
Suppose there is a wall 9 chi high. A melon vine grows from the top of the wall, extending downward at a rate of 7 cun per day. A bottle gourd vine grows from the bottom of the wall, extending upward at a rate of 1 chi per day.
Question: after how many days do they meet? How long are the melon vine and the bottle gourd vine at that time?

The procedure says: Suppose 5 days, the gap is less than 5 cun. Suppose 6 days, the gap exceeds 1 chi 2 cun.

Answer: *a*(=90/17) days. The melon vine is *b*(=63/17) chi long, and the bottle gourd vine is *c*(=90/17) chi long.
"""

# 垣高九尺
垣高 = 9

# 瓜蔓日長七寸
瓜日長 = Fraction(7, 10)  # Convert 7 cun to chi

# 瓠蔓日長一尺
瓠日長 = 1

# 瓜、瓠每日靠近的距離
每日靠近距離 = 瓠日長 + 瓜日長

# 問：幾何日相逢？
# 總距離為垣高，時間為距離除以每日靠近距離
a = Fraction(垣高, 每日靠近距離)  # 90/17 days

# 瓜長
b = 瓜日長 * a  # 63/17 chi

# 瓠長
c = 瓠日長 * a  # 90/17 chi
"""
"""
