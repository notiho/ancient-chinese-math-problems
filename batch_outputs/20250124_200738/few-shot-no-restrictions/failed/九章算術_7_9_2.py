"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
術曰：假令五日，不足五寸。令之六日，有餘一尺二寸。
荅曰： a日 。瓜長 b尺 ，瓠長 c尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 9 chi high. A melon vine grows from the top of the wall, extending downward at a rate of 7 cun per day. A bottle gourd vine grows from the bottom of the wall, extending upward at a rate of 1 chi per day.
Question: After how many days will the two vines meet? How long will the melon vine and the bottle gourd vine be at that time?

The procedure says: Suppose 5 days pass, the vines are 5 cun short of meeting. Suppose 6 days pass, the vines exceed the meeting point by 1 chi and 2 cun.

Answer: *a* days. The melon vine is *b* chi long, and the bottle gourd vine is *c* chi long.
"""

from fractions import Fraction

# 垣高九尺
垣高 = 9  # chi

# 瓜蔓日長七寸
瓜蔓日長 = Fraction(7, 10)  # chi per day (7 cun = 7/10 chi)

# 瓠蔓日長一尺
瓠蔓日長 = 1  # chi per day

# Relative growth rate per day (combined growth of both vines)
相對增長 = 瓜蔓日長 + 瓠蔓日長

# Total distance to meet (垣高)
距離 = 垣高

# 幾何日相逢？
a = 距離 / 相對增長  # days

# 瓜長 b尺
b = 瓜蔓日長 * a  # chi

# 瓠長 c尺
c = 瓠蔓日長 * a  # chi

# Final results
a = float(a)
b = float(b)
c = float(c)

a, b, c  # Output: days, melon vine length, bottle gourd vine length#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 90/17, Actual: 5.294117647058823
Variable 'b' has wrong value. Expected: 63/17, Actual: 3.7058823529411766
Variable 'c' has wrong value. Expected: 90/17, Actual: 5.294117647058823"""
