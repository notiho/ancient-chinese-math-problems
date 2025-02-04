"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
術曰：置四分日之三，除三分日之一，半其餘以為法。副置法，增三分日之一，以三百里乘之，為實。實如法，得主人馬一日行。
荅曰： a(=780)里 。
"""

#----- content starts here -----
"""
Suppose there is a guest's horse that travels 300 li per day. 
The guest departs but forgets to bring their clothes. After 1/3 of the day has passed, the host realizes this.
The host takes the clothes, catches up with the guest, gives them the clothes, and returns home. 
By the time the host returns home, 3/4 of the day has passed.
Question: how far does the host's horse travel in one day, assuming it does not rest?

The procedure says: Place 3/4 of the day, divide it by 1/3 of the day, and halve the remainder to obtain the divisor.
Place the divisor again, add 1/3 of the day, and multiply it by 300 li to obtain the dividend.
Divide the dividend by the divisor to obtain the distance the host's horse travels in one day.

Answer: *a*(=780) li.
"""

from fractions import Fraction

# 客馬日行三百里
客馬日行 = 300

# 日已三分之一
客行時間 = Fraction(1, 3)

# 至家視日四分之三
主人總時間 = Fraction(3, 4)

# 置四分日之三，除三分日之一
餘時間 = 主人總時間 / 客行時間

# 半其餘以為法
法 = Fraction(餘時間 - 1, 2)

# 副置法，增三分日之一
法增 = 法 + 客行時間

# 以三百里乘之，為實
實 = 法增 * 客馬日行

# 實如法，得主人馬一日行
a = Fraction(實, 法) # 780
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 780, Actual: 460"""
