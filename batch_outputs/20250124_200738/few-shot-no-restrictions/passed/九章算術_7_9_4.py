"""
今有垣高九尺。瓜生其上，蔓日長七寸。瓠生其下，蔓日長一尺。問︰幾何日相逢？瓜、瓠各長幾何？
術曰：假令五日，不足五寸。令之六日，有餘一尺二寸。
荅曰： a日 。瓜長 b尺 ，瓠長 c尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 9 chi high. A melon vine grows from the top of the wall, extending downward at a rate of 7 cun per day. A gourd vine grows from the bottom of the wall, extending upward at a rate of 1 chi per day. 
Question: After how many days will the two vines meet? How long will each vine be at that time?

The procedure says: Assume 5 days, and the gap is still 5 cun. Assume 6 days, and the overlap is 1 chi 2 cun.

Answer: *a* days. The melon vine is *b* chi long, and the gourd vine is *c* chi long.
"""

# 垣高九尺
垣高 = 9  # chi

# 瓜蔓日長七寸
瓜蔓日長 = Fraction(7, 10)  # chi per day (7 cun = 7/10 chi)

# 瓠蔓日長一尺
瓠蔓日長 = 1  # chi per day

# 瓜、瓠蔓相對增長速度
相對增長速度 = 瓠蔓日長 + 瓜蔓日長  # chi per day

# 問：幾何日相逢？
a = 垣高 / 相對增長速度  # days

# 瓜長
b = 瓜蔓日長 * a  # chi

# 瓠長
c = 瓠蔓日長 * a  # chi

# Final results
a = Fraction(a).limit_denominator()  # Convert to fraction for exact representation
b = Fraction(b).limit_denominator()
c = Fraction(c).limit_denominator()

a, b, c  # Output the results#----- content ends here -----

"""
"""
