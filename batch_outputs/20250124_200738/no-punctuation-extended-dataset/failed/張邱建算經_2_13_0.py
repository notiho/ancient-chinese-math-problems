"""
今有粟米三千斛六百人食之其一百人日食糳米八斛二百人日食粺米十四斛三百人日食糲米十八斛問粟得㡬何日食之
術曰置粟數為實以三等日食米積數各求為粟之數併以為法實如法而一
答曰 a日
"""

#----- content starts here -----
"""
Suppose there are 3000 hu of millet, and 600 people consume it.
Among them:
- 100 people consume 8 hu of coarse millet per day,
- 200 people consume 14 hu of semi-polished millet per day,
- 300 people consume 18 hu of roughly husked millet per day.
Question: for how many days can the millet last?

The procedure says: Place the amount of millet as the dividend.
For each of the three groups, calculate the millet required to produce their daily consumption of rice.
Sum these to form the divisor.
Divide the dividend by the divisor to obtain the number of days.

Answer: *a* days.
"""

from fractions import Fraction

# 粟米三千斛
粟 = 3000

# 600人分為三等
第一等人數 = 100
第二等人數 = 200
第三等人數 = 300

# 每日食米量
第一等日食糳米 = 8
第二等日食粺米 = 14
第三等日食糲米 = 18

# 粟轉化為糳米、粺米、糲米的比例
糳米比例 = Fraction(4, 5)  # 粟 5 -> 糳米 4
粺米比例 = Fraction(3, 4)  # 粟 4 -> 粺米 3
糲米比例 = Fraction(3, 5)  # 粟 5 -> 糲米 3

# 各等每日所需粟數
第一等每日粟需求 = 第一等日食糳米 / 糳米比例
第二等每日粟需求 = 第二等日食粺米 / 粺米比例
第三等每日粟需求 = 第三等日食糲米 / 糲米比例

# 合計每日粟需求
每日粟需求 = 第一等每日粟需求 + 第二等每日粟需求 + 第三等每日粟需求

# 粟數除以每日需求，得可食天數
a = Fraction(粟, 每日粟需求)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2025/49, Actual: 1125/22"""
