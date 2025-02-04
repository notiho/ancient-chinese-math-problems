"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
術曰：置四分日之三，除三分日之一，半其餘以為法。副置法，增三分日之一，以三百里乘之，為實。實如法，得主人馬一日行。
荅曰： a(=780)里 。
"""

#----- content starts here -----
"""
Suppose there is a guest whose horse travels 300 li per day. The guest departs but forgets to bring their clothes.
After 1/3 of the day has passed, the host realizes this. The host takes the clothes, chases the guest, catches up, gives the clothes, and returns home.
When the host arrives back home, 3/4 of the day has passed.
Question: How far does the host's horse travel in one day, assuming it does not rest?

The procedure says: Place 3/4 of the day and divide it by 1/3 of the day. Halve the remainder to obtain the divisor.
Place the divisor again, add 1/3 of the day, and multiply by 300 li to obtain the dividend.
Divide the dividend by the divisor to find the distance the host's horse travels in one day.

Answer: *a*(=780) li.
"""

from fractions import Fraction

# 客馬日行三百里
客馬日行 = 300

# 日已三分之一
客已行日 = Fraction(1, 3)

# 至家視日四分之三
主人總用日 = Fraction(3, 4)

# 置四分日之三，除三分日之一
法 = 主人總用日 / 客已行日

# 半其餘以為法
法 = (法 - 1) / 2

# 副置法，增三分日之一
法 = 法 + 1

# 以三百里乘之，為實
實 = 客馬日行 * 法

# 實如法，得主人馬一日行
a = 實 / 法 # 780#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 780, Actual: 300"""
