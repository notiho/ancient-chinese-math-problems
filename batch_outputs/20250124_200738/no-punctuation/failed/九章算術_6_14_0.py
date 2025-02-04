"""
今有人持金十二斤出關關稅之十分而取一今關取金二斤償錢五千問金一斤值錢幾何
術曰以一十乘二斤以十二斤減之餘為法以一十乘五千為實實如法得一錢
荅曰 a 
"""

#----- content starts here -----
"""
Suppose someone carries 12 jin of gold out of the pass. The pass tax is one-tenth of the gold.
Now the pass takes 2 jin of gold and compensates with 5000 qian.
Question: how much is 1 jin of gold worth in qian?

The procedure says: Multiply 10 by the 2 jin [of gold taken as tax]. Subtract it from 12 jin, and the remainder is the divisor.
Multiply 10 by 5000 qian, and this is the dividend.
Divide the dividend by the divisor to obtain the value of 1 jin of gold in qian.

The answer says: *a* qian.
"""

# 金十二斤
金總 = 12

# 關取金二斤
關取金 = 2

# 償錢五千
償錢 = 5000

# 以一十乘二斤
實 = 10 * 關取金

# 以十二斤減之，餘為法
法 = 金總 - 關取金

# 以一十乘五千為實
實 = 10 * 償錢

# 實如法得一錢
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6250, Actual: 5000"""
