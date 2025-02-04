"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
術曰：置四分日之三，除三分日之一，半其餘以為法。副置法，增三分日之一，以三百里乘之，為實。實如法，得主人馬一日行。
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a guest's horse that travels 300 li per day. The guest departs but forgets to take their clothes. After 1/3 of the day has passed, the host realizes this. The host takes the clothes, catches up with the guest, gives them the clothes, and then returns home. Upon returning home, the host sees that 3/4 of the day has passed. The host's horse does not rest.

Question: How many li does the host's horse travel in one day?

The procedure says: Place 3/4 of the day, divide it by 1/3 of the day, and halve the remainder to obtain the divisor. Place the divisor again, add 1/3 of the day to it, and multiply it by 300 li to obtain the dividend. Divide the dividend by the divisor to find the distance the host's horse travels in one day.

Answer: The host's horse travels *a* li in one day.
"""

from fractions import Fraction

# Guest's horse travels 300 li per day
客馬日行 = 300

# Time passed before the host realized (1/3 of the day)
已過時間 = Fraction(1, 3)

# Time passed when the host returned home (3/4 of the day)
返回時間 = Fraction(3, 4)

# Step 1: 置四分日之三，除三分日之一
時間比 = 返回時間 / 已過時間

# Step 2: 半其餘以為法
法 = (時間比 - 1) / 2

# Step 3: 副置法，增三分日之一
法增 = 法 + 已過時間

# Step 4: 以三百里乘之，為實
實 = 法增 * 客馬日行

# Step 5: 實如法，得主人馬一日行
a = 實 / 法

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 780, Actual: 460"""
