"""
今有粟米三千斛六百人食之其一百人日食糳米八斛二百人日食粺米十四斛三百人日食糲米十八斛問粟得㡬何日食之
術曰置粟數為實以三等日食米積數各求為粟之數併以為法實如法而一
答曰 a日
"""

"""
Suppose there are 3000 hu of millet, and 600 people are eating it.
Among them:
- 100 people eat 8 hu of coarse millet per day,
- 200 people eat 14 hu of semi-polished millet per day,
- 300 people eat 18 hu of roughly husked millet per day.
Question: how many days can the millet last?

The procedure says: Place the amount of millet as the dividend.
For each of the three groups, calculate the millet required per day for their respective types of millet.
Sum these to obtain the divisor.
Divide the dividend by the divisor to obtain the number of days.

Answer: *a* days.
"""

# 粟米三千斛
粟 = 3000

# 600人食之
總人數 = 600

# 各等人數與日食量
第一等人數 = 100
第一等日食量 = 8

第二等人數 = 200
第二等日食量 = 14

第三等人數 = 300
第三等日食量 = 18

# 各等日食米積數
第一等日食米積數 = 第一等人數 * 第一等日食量
第二等日食米積數 = 第二等人數 * 第二等日食量
第三等日食米積數 = 第三等人數 * 第三等日食量

# 各求為粟之數併以為法
法 = 第一等日食米積數 + 第二等日食米積數 + 第三等日食米積數

# 實如法而一
a = Fraction(粟, 法)
"""
Variable 'a' has wrong value. Expected: 2025/49, Actual: 1/3"""
