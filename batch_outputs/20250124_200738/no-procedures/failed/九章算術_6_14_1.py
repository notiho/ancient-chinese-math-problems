"""
今有人持金十二斤出關。關稅之，十分而取一。今關取金二斤，償錢五千。問︰金一斤值錢幾何？
荅曰： a 。
"""

#----- content starts here -----
"""
Suppose someone carries 12 jin of gold out of the border. The border tax takes 1/10 of the gold. 
Now the border takes 2 jin of gold and compensates with 5000 qian. 
Question: how much is 1 jin of gold worth in qian?

Answer: *a* qian.
"""

# 金十二斤
金總量 = 12

# 關稅之，十分而取一
關稅比例 = Fraction(1, 10)

# 關取金二斤，償錢五千
關取金 = 2
償錢 = 5000

# Calculate the value of 1 jin of gold
# The value of 2 jin of gold is equal to the compensation money (5000 qian)
# Therefore, the value of 1 jin of gold is:
a = Fraction(償錢, 關取金)

# Result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6250, Actual: 2500"""
