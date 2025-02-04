"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
術曰：置四分日之三，除三分日之一，半其餘以為法。副置法，增三分日之一，以三百里乘之，為實。實如法，得主人馬一日行。
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a guest's horse that travels 300 li per day. The guest departs but forgets to bring their clothing. After 1/3 of the day has passed, the host realizes this. The host takes the clothing, catches up with the guest, gives it to them, and then returns home. Upon returning home, the host observes that 3/4 of the day has passed.

Question: If the host's horse does not rest, how far does it travel in one day?

The procedure says:
- Take 3/4 of the day and divide it by 1/3 of the day. Halve the remainder to obtain the divisor (法).
- Place the divisor (法) again, add 1/3 of the day to it, and multiply by 300 li to obtain the dividend (實).
- Divide the dividend (實) by the divisor (法) to find the distance the host's horse travels in one day.

Answer: *a* li.
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
法 += 1

# 以三百里乘之，為實
實 = 客馬日行 * 法

# 實如法，得主人馬一日行
a = 實 / 法

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 780, Actual: 300"""
