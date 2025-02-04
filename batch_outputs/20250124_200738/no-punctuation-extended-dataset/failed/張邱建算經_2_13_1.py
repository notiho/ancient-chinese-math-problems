"""
今有粟米三千斛六百人食之其一百人日食糳米八斛二百人日食粺米十四斛三百人日食糲米十八斛問粟得㡬何日食之
術曰置粟數為實以三等日食米積數各求為粟之數併以為法實如法而一
答曰 a日
"""

#----- content starts here -----
"""
Suppose there are 3000 hu of millet and 600 people consuming it.
Among them:
- 100 people consume 8 hu of coarse millet per day,
- 200 people consume 14 hu of medium-milled millet per day,
- 300 people consume 18 hu of roughly husked millet per day.
Question: how many days can the millet last?

The procedure says: Place the amount of millet as the dividend.
For each of the three groups, calculate the millet required for their daily consumption by converting their rice consumption back into millet.
Add these together to form the divisor.
Divide the dividend by the divisor to obtain the number of days.

Answer: *a* days.
"""

from fractions import Fraction

# 粟米三千斛
粟 = 3000

# 600人食之
總人數 = 600

# 各等日食米數
糳米日食 = 8  # 100人日食糳米8斛
粺米日食 = 14  # 200人日食粺米14斛
糲米日食 = 18  # 300人日食糲米18斛

# 各等人數
糳米人數 = 100
粺米人數 = 200
糲米人數 = 300

# 各等日食粟之數
# 粟與米的轉換比例假設為1:1（題目未明確給出轉換比例，直接使用日食數據）
糳米粟日食 = 糳米人數 * 糳米日食
粺米粟日食 = 粺米人數 * 粺米日食
糲米粟日食 = 糲米人數 * 糲米日食

# 併以為法
法 = 糳米粟日食 + 粺米粟日食 + 糲米粟日食

# 實如法而一
a = Fraction(粟, 法)  # 得到粟可食用的天數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2025/49, Actual: 1/3"""
