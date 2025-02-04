"""
今有人持金十二斤出關。關稅之，十分而取一。今關取金二斤，償錢五千。問︰金一斤值錢幾何？
荅曰： a 。
"""

#----- content starts here -----
"""
Suppose someone carries 12 jin of gold out of the border. The border tax is 1/10 of the gold.
The border collects 2 jin of gold and compensates with 5000 qian. 
Question: how much is 1 jin of gold worth in qian?

Answer: *a* qian.
"""

# 金十二斤
total_gold = 12

# 關取金二斤，償錢五千
gold_taken = 2
money_compensated = 5000

# The value of 2 jin of gold is equivalent to the 2 jin taken + the 5000 qian compensated
value_of_2_jin = gold_taken + Fraction(money_compensated, 1000)

# The value of 1 jin of gold
a = Fraction(value_of_2_jin, 2)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 6250, Actual: 7/2"""
