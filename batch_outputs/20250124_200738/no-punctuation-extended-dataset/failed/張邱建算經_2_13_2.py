"""
今有粟米三千斛六百人食之其一百人日食糳米八斛二百人日食粺米十四斛三百人日食糲米十八斛問粟得㡬何日食之
術曰置粟數為實以三等日食米積數各求為粟之數併以為法實如法而一
答曰 a日
"""

#----- content starts here -----
"""
Suppose there are 3000 hu of millet, and 600 people consume it.
Among them:
- 100 people consume 8 hu of coarse rice daily,
- 200 people consume 14 hu of semi-polished rice daily,
- 300 people consume 18 hu of roughly husked rice daily.
Question: for how many days can the millet sustain them?

The procedure says: Place the amount of millet as the dividend.
For the three groups, calculate the daily rice consumption and convert each into millet consumption.
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

# 各求為粟之數
# 粟與米的比例：糳米三之五，粺米三之四，糲米三之三
糳米粟率 = Fraction(5, 3)
粺米粟率 = Fraction(4, 3)
糲米粟率 = Fraction(3, 3)

# 各等日食粟數
糳米日食粟 = 糳米日食 * 糳米粟率
粺米日食粟 = 粺米日食 * 粺米粟率
糲米日食粟 = 糲米日食 * 糲米粟率

# 各等人數的總日食粟數
糳米總日食粟 = 糳米人數 * 糳米日食粟
粺米總日食粟 = 粺米人數 * 粺米日食粟
糲米總日食粟 = 糲米人數 * 糲米日食粟

# 併以為法
法 = 糳米總日食粟 + 粺米總日食粟 + 糲米總日食粟

# 實如法而一
a = Fraction(粟, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2025/49, Actual: 45/157"""
