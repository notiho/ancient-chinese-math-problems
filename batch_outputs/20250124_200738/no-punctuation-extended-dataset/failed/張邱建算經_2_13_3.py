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
- 200 people consume 14 hu of medium rice daily,
- 300 people consume 18 hu of fine rice daily.
Question: For how many days can the millet sustain them?

The procedure says:
Place the amount of millet as the dividend.
For each of the three groups, calculate the amount of millet required to produce their daily rice consumption.
Sum these to form the divisor.
Divide the dividend by the divisor to find the number of days.

Answer: *a* days.
"""

from fractions import Fraction

# 粟米三千斛
粟 = 3000

# 600人分為三等
第一等人數 = 100
第二等人數 = 200
第三等人數 = 300

# 每日食米
第一等日食米 = 8
第二等日食米 = 14
第三等日食米 = 18

# 各求為粟之數
第一等日食粟 = Fraction(第一等日食米, 4)  # 粟 to coarse rice ratio: 4:1
第二等日食粟 = Fraction(第二等日食米, 5)  # 粟 to medium rice ratio: 5:1
第三等日食粟 = Fraction(第三等日食米, 3)  # 粟 to fine rice ratio: 3:1

# 各等日食粟積數
第一等日食粟積數 = 第一等人數 * 第一等日食粟
第二等日食粟積數 = 第二等人數 * 第二等日食粟
第三等日食粟積數 = 第三等人數 * 第三等日食粟

# 併以為法
法 = 第一等日食粟積數 + 第二等日食粟積數 + 第三等日食粟積數

# 實如法而一
a = Fraction(粟, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2025/49, Actual: 75/64"""
