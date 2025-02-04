"""
今有次官田五十七畞一百五十步畞别計米五斗輸官官亦令納穀三斛準米一斛四斗問米及穀各幾何
術曰置畞數以二百四十步乗之内一百五十步得一萬三千八百三十步為實以次田法四百八十步除之得米數欲求穀以三斛因米得八十六斛四斗三升七合五勺以米一斛四斗除之得穀數不盡者與法俱倍之命分何以知次田四百八十步為法術曰置二百四十步於上米五斗為法而一得四十八步以為一斗之法上十之為四百八十步即斛法欲知田一步計米二合一十二分合之一術曰置米五斗再上十之為五百合為實以二百四十步除之得二合不盡者退位與法俱半之命分即見毎步之法
答曰米 a斛 穀 b斛
"""

"""
Suppose there is a subordinate official's field of 57 mu and 150 bu. Each mu is calculated to yield 5 dou of rice. The official also requires the payment of 3 hu of grain, where 1 hu of grain is equivalent to 4 dou of rice. 
Question: How much rice and grain should be paid?

The procedure says: Place the number of mu and multiply it by 240 bu (the number of bu in one mu). Add the remaining 150 bu, obtaining 13,830 bu as the total. Use the subordinate official's field divisor of 480 bu to divide it, obtaining the amount of rice. 
To find the amount of grain, use 3 hu as the base and convert the rice into grain. Multiply the rice by 3 hu and divide by 1 hu = 4 dou, obtaining the amount of grain. If there is a remainder, multiply both the remainder and the divisor to scale up for fractional parts.

The answer says: *a* hu of rice, *b* hu of grain.
"""

from fractions import Fraction

# 次官田五十七畞一百五十步
畞數 = 57
餘步 = 150

# 每畞二百四十步
每畞步數 = 240

# 每畞計米五斗
每畞米 = 5

# 官令納穀三斛，準米一斛四斗
穀斛 = 3
穀斛米斗 = 4

# 置畞數以二百四十步乘之，內一百五十步
總步數 = 畞數 * 每畞步數 + 餘步

# 次田法四百八十步
次田法 = 480

# 以次田法四百八十步除之，得米數
米數斗 = Fraction(總步數, 次田法) * 每畞米

# 將米數轉換為斛
米數斛 = Fraction(米數斗, 10)

# 欲求穀，以三斛因米得
穀數斛 = 米數斛 * 穀斛 / 穀斛米斗

# 答
a = 米數斛
b = 穀數斛
"""
Variable 'a' has wrong value. Expected: 461/16, Actual: 461/32
Variable 'b' has wrong value. Expected: 6915/112, Actual: 1383/128"""
