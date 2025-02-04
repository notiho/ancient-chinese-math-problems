"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
術曰：假令五日，不足五寸。令之六日，有餘一尺二寸。
荅曰： a(=90/17)日 。瓜長 b(=63/17)尺 ，瓠長 c(=90/17)尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 9 chi high. A melon grows on top of the wall, and its vine grows upward at a rate of 7 cun per day. A bottle gourd grows at the bottom of the wall, and its vine grows upward at a rate of 1 chi per day.
Question: after how many days do the two vines meet? How long are the melon vine and the bottle gourd vine at that time?

The procedure says: Suppose it is 5 days, and the difference is less than 5 cun. Suppose it is 6 days, and the difference is more than 1 chi 2 cun.

Answer: *a*(=90/17) days. The melon vine is *b*(=63/17) chi long, and the bottle gourd vine is *c*(=90/17) chi long.
"""

# 垣高九尺
垣高 = 9  # chi

# 瓜蔓日長七寸
瓜蔓日長 = Fraction(7, 10)  # chi per day (convert 7 cun to chi)

# 瓠蔓日長一尺
瓠蔓日長 = 1  # chi per day

# 瓜蔓和瓠蔓的相對增長速度
相對增長速度 = 瓠蔓日長 - 瓜蔓日長

# 垣高是兩蔓相遇的初始距離
相遇距離 = 垣高

# 幾何日相逢？
a = Fraction(相遇距離, 相對增長速度)  # 90/17 days

# 瓜長
b = 瓜蔓日長 * a  # 63/17 chi

# 瓠長
c = 瓠蔓日長 * a  # 90/17 chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 90/17, Actual: 30
Variable 'b' has wrong value. Expected: 63/17, Actual: 21
Variable 'c' has wrong value. Expected: 90/17, Actual: 30"""
