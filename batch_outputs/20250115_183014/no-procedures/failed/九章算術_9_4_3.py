"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
荅曰： a丈 。
"""

"""
Suppose there is a tree 2 zhang tall, with a circumference of 3 chi. A vine grows from the base of the tree, spiraling around it 7 times, and reaches the top of the tree.  
Question: how long is the vine?

Answer: the vine is *a* zhang long.
"""

# 木長二丈
木長 = 2  # in zhang

# 圍之三尺
圍 = 3  # in chi

# 葛纏木七周
纏周 = 7

# 葛生的長度是螺旋的斜邊，根據勾股定理計算
# 每一周的水平距離是圍 (circumference), 垂直距離是木長 / 纏周
水平距離 = 圍  # in chi
垂直距離 = 木長 * 10 / 纏周  # convert 木長 to chi (1 zhang = 10 chi)

# 每一周的斜邊長度
單周長度 = (水平距離**2 + 垂直距離**2)**0.5

# 總長度
總長度 = 單周長度 * 纏周  # in chi

# Convert the total length back to zhang
a = Fraction(總長度, 10)  # 1 zhang = 10 chi

a  # 葛長 in zhang
"""
Code error: both arguments should be Rational instances"""
