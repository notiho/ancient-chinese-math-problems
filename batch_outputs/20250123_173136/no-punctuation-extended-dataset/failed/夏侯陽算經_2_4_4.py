"""
今有次官田五十七畞一百五十步畞别計米五斗輸官官亦令納穀三斛準米一斛四斗問米及穀各幾何
術曰置畞數以二百四十步乗之内一百五十步得一萬三千八百三十步為實以次田法四百八十步除之得米數欲求穀以三斛因米得八十六斛四斗三升七合五勺以米一斛四斗除之得穀數不盡者與法俱倍之命分何以知次田四百八十步為法術曰置二百四十步於上米五斗為法而一得四十八步以為一斗之法上十之為四百八十步即斛法欲知田一步計米二合一十二分合之一術曰置米五斗再上十之為五百合為實以二百四十步除之得二合不盡者退位與法俱半之命分即見毎步之法
答曰米 a斛 穀 b斛
"""

"""
Suppose there is a field of 57 mu and 150 bu. For each mu, 5 dou of rice is calculated. The officials also require the delivery of 3 hu of grain, where 1 hu is equivalent to 4 dou of rice.
Question: how much rice and grain should be delivered?

The procedure says:
1. Place the number of mu and multiply it by 240 bu. Add 150 bu to it, obtaining 13830 bu as the total area.
2. Divide this by the "secondary field divisor" of 480 bu, obtaining the amount of rice.
3. To find the grain, multiply 3 hu by the amount of rice, obtaining 86 hu, 4 dou, 3 sheng, 7 ge, and 5 jue. Divide this by the conversion factor of 1 hu = 4 dou, obtaining the amount of grain.
4. If there is a remainder, multiply both the remainder and the divisor by the same factor to express it as a fraction.

How is the "secondary field divisor" of 480 bu determined?
The procedure says:
1. Place 240 bu above and 5 dou of rice as the divisor. Divide, obtaining 48 bu as the amount corresponding to 1 dou.
2. Multiply this by 10, obtaining 480 bu as the divisor for 1 hu.

How is the rice per bu determined?
The procedure says:
1. Place 5 dou of rice and multiply it by 10, obtaining 500 ge as the total.
2. Divide this by 240 bu, obtaining 2 ge per bu.
3. If there is a remainder, reduce the unit and divide again, obtaining the fractional part.

Answer: *a* hu of rice, *b* hu of grain.
"""

from fractions import Fraction

# 次官田五十七畞一百五十步
畞數 = 57
餘步 = 150

# 每畞二百四十步
每畞步 = 240

# 計算田的總步數
總步數 = 畞數 * 每畞步 + 餘步  # 置畞數以二百四十步乘之，內一百五十步

# 次田法四百八十步
次田法 = 480

# 以次田法除之，得米數
米數 = Fraction(總步數, 次田法)

# 官令納穀三斛，準米一斛四斗
穀率 = 3  # 每米斛數
米斛斗 = 4  # 一斛等於四斗

# 計算穀數
穀數 = 穀率 * 米數  # 以三斛因米得穀數

# 答案
a = 米數  # 米 a斛
b = 穀數  # 穀 b斛
"""
Variable 'b' has wrong value. Expected: 6915/112, Actual: 1383/16"""
