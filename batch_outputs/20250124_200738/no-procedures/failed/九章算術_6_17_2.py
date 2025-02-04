"""
今有五人分五錢，令上二人所得與下三人等。問︰各得幾何？
荅曰：甲得 a錢 ，乙得 b錢 ，丙得 c錢 ，丁得 d錢 ，戊得 e錢 。
"""

#----- content starts here -----
"""
Suppose there are 5 people dividing 5 qian (錢). The condition is that the sum of the amounts received by the first two people (the "upper two") must equal the sum of the amounts received by the last three people (the "lower three").
Question: how much does each person get?

Answer: Jia (甲) gets *a* qian, Yi (乙) gets *b* qian, Bing (丙) gets *c* qian, Ding (丁) gets *d* qian, Wu (戊) gets *e* qian.
"""

from fractions import Fraction

# Total money
total_money = 5

# Let the amounts received by Jia, Yi, Bing, Ding, and Wu be a, b, c, d, and e respectively.
# Condition 1: a + b + c + d + e = 5
# Condition 2: a + b = c + d + e

# From Condition 2, we can express c + d + e as a + b.
# Substituting into Condition 1: a + b + (a + b) = 5
# Simplify: 2(a + b) = 5
# Solve for a + b: a + b = 5 / 2

# The remaining money for c, d, and e is also 5 / 2, and we assume they split it equally.
a_plus_b = Fraction(5, 2)
c_plus_d_plus_e = Fraction(5, 2)

# Split c, d, and e equally
c = d = e = c_plus_d_plus_e / 3

# Split a and b equally
a = b = a_plus_b / 2

# Final results
print(f"甲 (Jia) 得: {a} 錢")
print(f"乙 (Yi) 得: {b} 錢")
print(f"丙 (Bing) 得: {c} 錢")
print(f"丁 (Ding) 得: {d} 錢")
print(f"戊 (Wu) 得: {e} 錢")#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4/3, Actual: 5/4
Variable 'b' has wrong value. Expected: 7/6, Actual: 5/4
Variable 'c' has wrong value. Expected: 1, Actual: 5/6
Variable 'e' has wrong value. Expected: 2/3, Actual: 5/6"""
