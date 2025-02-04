"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
術曰：置四分日之三，除三分日之一，半其餘以為法。副置法，增三分日之一，以三百里乘之，為實。實如法，得主人馬一日行。
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a traveler whose horse travels 300 li per day. The traveler forgot to bring their clothes, and after 1/3 of the day had passed, the host realized it. The host then took the clothes, caught up with the traveler, handed them over, and returned home. Upon returning home, they saw that 3/4 of the day had passed.
Question: if the host's horse did not rest, how far does it travel in one day?

The procedure says: Place 3/4 of the day, divide it by 1/3 of the day, and halve the remainder to obtain the divisor.
Place the divisor again, add 1/3 of the day, and multiply it by 300 li to obtain the dividend.
Divide the dividend by the divisor to obtain the distance the host's horse travels in one day.

Answer: *a* li.
"""

from fractions import Fraction

# 日已三分之一
日三分之一 = Fraction(1, 3)

# 至家視日四分之三
日四分之三 = Fraction(3, 4)

# 置四分日之三，除三分日之一
商 = 日四分之三 / 日三分之一

# 半其餘以為法
法 = (商 - 1) / 2

# 副置法，增三分日之一
法增 = 法 + 日三分之一

# 以三百里乘之，為實
實 = 法增 * 300

# 實如法，得主人馬一日行
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 780, Actual: 460"""
