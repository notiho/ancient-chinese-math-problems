"""
今有客馬日行三百里。客去忘持衣，日已三分之一，主人乃覺。持衣追及與之而還，至家視日四分之三。問︰主人馬不休，日行幾何？
術曰：置四分日之三，除三分日之一，半其餘以為法。副置法，增三分日之一，以三百里乘之，為實。實如法，得主人馬一日行。
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a traveler's horse that travels 300 li per day. 
The traveler forgot to bring their clothes, and after 1/3 of the day had passed, the host realized it. 
The host then took the clothes, caught up with the traveler, gave them the clothes, and returned home. 
When the host returned home, 3/4 of the day had passed. 
Question: How far does the host's horse travel in one day, assuming it does not rest?

The procedure says: Place 3/4 of the day, divide it by 1/3 of the day, and take half of the remainder as the divisor.
Place the divisor again, add 1/3 of the day, and multiply it by 300 li to obtain the dividend.
Divide the dividend by the divisor to obtain the distance the host's horse travels in one day.

Answer: The host's horse travels *a* li in one day.
"""

from fractions import Fraction

# Known values
客馬日行 = 300  # li per day
日已三分之一 = Fraction(1, 3)  # 1/3 of the day
至家視日四分之三 = Fraction(3, 4)  # 3/4 of the day

# Step 1: 置四分日之三，除三分日之一
餘 = 至家視日四分之三 / 日已三分之一

# Step 2: 半其餘以為法
法 = Fraction(餘 - 1, 2)

# Step 3: 副置法，增三分日之一
增量 = 法 + 日已三分之一

# Step 4: 以三百里乘之，為實
實 = 客馬日行 * 增量

# Step 5: 實如法，得主人馬一日行
a = 實 / 法

a  # The host's horse travels this many li in one day.#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 780, Actual: 460"""
