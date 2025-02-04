"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
術曰：假令五日，不足五寸。令之六日，有餘一尺二寸。
荅曰： a日 。瓜長 b尺 ，瓠長 c尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 9 chi high. A melon vine grows from the top of the wall, and its vine grows 7 cun per day downward. 
A gourd vine grows from the bottom of the wall, and its vine grows 1 chi (10 cun) per day upward.
Question: after how many days do the two vines meet? How long are the melon and gourd vines respectively?

The procedure says: Suppose 5 days, the vines are 5 cun short of meeting. Suppose 6 days, the vines overlap by 1 chi 2 cun (12 cun).

Answer: *a* days. The melon vine is *b* chi long, and the gourd vine is *c* chi long.
"""

from fractions import Fraction

# 垣高九尺
垣高 = 9  # in chi

# 瓜蔓日長七寸
瓜蔓日長 = Fraction(7, 10)  # in chi (7 cun = 7/10 chi)

# 瓠蔓日長一尺
瓠蔓日長 = 1  # in chi

# 瓜蔓與瓠蔓每日靠近的距離
每日靠近距離 = 瓠蔓日長 + 瓜蔓日長

# 初始距離為垣高，計算相逢所需的天數
a = Fraction(垣高, 每日靠近距離)

# 瓜長
b = 瓜蔓日長 * a

# 瓠長
c = 瓠蔓日長 * a

# Output results
a_days = a
b_chi = b
c_chi = c

a_days, b_chi, c_chi#----- content ends here -----

"""
"""
