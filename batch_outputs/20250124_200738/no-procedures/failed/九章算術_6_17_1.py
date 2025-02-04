"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

#----- content starts here -----
"""
Suppose there are 5 people dividing 5 qian (錢). The condition is that the total amount received by the first two people (甲 and 乙) is equal to the total amount received by the last three people (丙, 丁, and 戊).
Question: how much does each person receive?

Answer: 甲 gets *a* qian, 乙 gets *b* qian, 丙 gets *c* qian, 丁 gets *d* qian, 戊 gets *e* qian.
"""

# Total qian
total_qian = 5

# Let the shares of 甲, 乙, 丙, 丁, 戊 be represented as a, b, c, d, e
# Condition 1: a + b = c + d + e
# Condition 2: a + b + c + d + e = total_qian

# Assign equal shares to satisfy the conditions
a = Fraction(5, 10)  # 甲 gets 1/2 qian
b = Fraction(5, 10)  # 乙 gets 1/2 qian
c = Fraction(5, 15)  # 丙 gets 1/3 qian
d = Fraction(5, 15)  # 丁 gets 1/3 qian
e = Fraction(5, 15)  # 戊 gets 1/3 qian

# Verify:
# a + b = c + d + e
# a + b + c + d + e = total_qian#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 1/2
Variable 'b' has wrong value. Expected: 7/6, Actual: 1/2
Variable 'c' has wrong value. Expected: 1, Actual: 1/3
Variable 'd' has wrong value. Expected: 5/6, Actual: 1/3
Variable 'e' has wrong value. Expected: 2/3, Actual: 1/3"""
