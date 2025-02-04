"""
今有人持金十二斤出關。關稅之，十分而取一。今關取金二斤，償錢五千。問︰金一斤值錢幾何？
術曰：以一十乘二斤，以十二斤減之，餘為法。以一十乘五千為實。實如法得一錢。
荅曰： a(=6250) 。
"""

#----- content starts here -----
"""
Suppose someone carries 12 jin of gold out of the pass. The customs tax is 1/10 of the amount.
Now, the customs takes 2 jin of gold and compensates with 5000 qian.
Question: how much is 1 jin of gold worth in qian?

The procedure says: Multiply 10 by the 2 jin of gold taken, then subtract 12 jin from it. The remainder is the divisor.
Multiply 10 by 5000 qian to get the dividend.
Divide the dividend by the divisor to obtain the value of 1 jin of gold in qian.

Answer: *a*(=6250) qian.
"""

# 金十二斤
金 = 12

# 關取金二斤
關取金 = 2

# 償錢五千
償錢 = 5000

# 以一十乘二斤
十乘二斤 = 10 * 關取金

# 以十二斤減之，餘為法
法 = 十乘二斤 - 金

# 以一十乘五千為實
實 = 10 * 償錢

# 實如法得一錢
a = Fraction(實, 法) # 6250#----- content ends here -----

"""
"""
