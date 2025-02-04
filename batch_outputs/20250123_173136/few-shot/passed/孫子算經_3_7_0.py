"""
今有絹，七萬八千七百三十二匹，令一百六十二人分之。問：人得幾何？
術曰：置絹七萬八千七百三十二匹為實，以一百六十二人為法。實如法，即得。
答曰： a匹 。
"""

"""
Suppose there are 78,732 bolts of silk, and 162 people are to divide them equally.
Question: how much does each person get?

The procedure says: Place the 78,732 bolts of silk as the dividend.
Take 162 people as the divisor.
Divide the dividend by the divisor, and the result is obtained.

Answer: each person gets *a* bolts of silk.
"""

# 置絹七萬八千七百三十二匹為實
實 = 78732

# 以一百六十二人為法
法 = 162

# 實如法，即得
a = Fraction(實, 法)
"""
"""
