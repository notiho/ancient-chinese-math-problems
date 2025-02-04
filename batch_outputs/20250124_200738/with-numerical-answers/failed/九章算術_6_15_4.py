"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
術曰：置四分日之三，除三分日之一，半其餘以為法。副置法，增三分日之一，以三百里乘之，為實。實如法，得主人馬一日行。
荅曰： a(=780)里 。
"""

#----- content starts here -----
"""
Suppose there is a guest's horse that travels 300 li in one day. 
The guest departs but forgets to bring clothing. After 1/3 of the day has passed, the host realizes this.
The host takes the clothing, catches up with the guest, gives it to them, and then returns home. 
When the host arrives back home, 3/4 of the day has passed.
Question: if the host's horse does not rest, how far does it travel in one day?

The procedure says: Place 3/4 of the day and divide it by 1/3 of the day. Halve the remainder to obtain the divisor.
Place the divisor again, add 1/3 of the day, and multiply it by 300 li to obtain the dividend.
Divide the dividend by the divisor to obtain the distance the host's horse travels in one day.

Answer: *a*(=780) li.
"""

from fractions import Fraction

# 客馬日行三百里
客馬日行 = 300

# 日已三分之一
日已 = Fraction(1, 3)

# 至家視日四分之三
至家 = Fraction(3, 4)

# 置四分日之三，除三分日之一
餘 = 至家 / 日已

# 半其餘以為法
法 = 餘 / 2

# 副置法，增三分日之一
增量 = 法 + 日已

# 以三百里乘之，為實
實 = 客馬日行 * 增量

# 實如法，得主人馬一日行
a = Fraction(實, 法)  # 780 li#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 780, Actual: 3500/9"""
