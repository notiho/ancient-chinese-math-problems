"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
術曰：置四分日之三，除三分日之一，半其餘以為法。副置法，增三分日之一，以三百里乘之，為實。實如法，得主人馬一日行。
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a guest's horse that travels 300 li in one day. The guest leaves but forgets to take their clothes. After 1/3 of the day has passed, the host realizes this. The host takes the clothes, catches up with the guest, gives the clothes, and returns home. By the time the host returns home, 3/4 of the day has passed. The host's horse does not rest.
Question: how far does the host's horse travel in one day?

The procedure says: Place 3/4 of the day, divide it by 1/3 of the day, and halve the remainder to obtain the divisor. Place the divisor again, add 1/3 of the day, and multiply it by 300 li to obtain the dividend. Divide the dividend by the divisor to get the distance the host's horse travels in one day.

Answer: The host's horse travels *a* li in one day.
"""

from fractions import Fraction

# 客馬日行三百里
客馬日行 = 300

# 日已三分之一
客已行時間 = Fraction(1, 3)

# 至家視日四分之三
主人總用時間 = Fraction(3, 4)

# 置四分日之三，除三分日之一
法 = 主人總用時間 / 客已行時間

# 半其餘以為法
法 = (法 - 1) / 2

# 副置法，增三分日之一
法 += 客已行時間

# 以三百里乘之，為實
實 = 客馬日行 * 法

# 實如法，得主人馬一日行
a = 實 / 法

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 780, Actual: 300"""
