"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
術曰：置四分日之三，除三分日之一，半其餘以為法。副置法，增三分日之一，以三百里乘之，為實。實如法，得主人馬一日行。
荅曰： a里 。
"""

"""
Suppose there is a guest whose horse travels 300 li per day. The guest left but forgot to bring their clothes.
After 1/3 of the day had passed, the host realized this and set out to chase the guest, delivering the clothes and returning home.
When the host returned home, 3/4 of the day had passed.
Question: if the host's horse did not rest, how far does it travel in one day?

The procedure says: Place 3/4 of the day, divide it by 1/3 of the day, and halve the remainder to make the divisor.
Place the divisor again, add 1/3 of the day, and multiply it by 300 li to make the dividend.
Divide the dividend by the divisor to obtain the host's horse's daily travel distance.

Answer: *a* li.
"""

from fractions import Fraction

# 日已三分之一
客行時間 = Fraction(1, 3)

# 至家視日四分之三
主人總時間 = Fraction(3, 4)

# 置四分日之三，除三分日之一
時間比 = 主人總時間 / 客行時間

# 半其餘以為法
法 = (時間比 - 1) / 2

# 副置法，增三分日之一
法增 = 法 + 客行時間

# 以三百里乘之，為實
客馬日行 = 300
實 = 法增 * 客馬日行

# 實如法，得主人馬一日行
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 780, Actual: 460"""
