"""
今有下官田八十九畞一百九十五步畞别計米四斗輸官官亦令納榖三斛準米一斛四斗問合計米及穀幾何
術曰置田畞數以二百四十步乗之内一百九十五步得二萬一千五百五十五步為實以下田斛法六百步除之得米數欲求穀者以三斛因米得一百七斛七斗七升五合為實以一斛四斗除為穀數不盡者命分何以知下田六百步為法術曰置二百四十步以米四斗為法除得六十步為一斗之法上十之為六百步乃為一斛之法欲知下田一步計米一合三分合之二術曰置米四斗再上十之為四百合為實以二百四十步除之得一合不盡者與法俱八約之命分
答曰米 a斛 穀 b斛
"""

#----- content starts here -----
"""
Suppose there is a lower official's field of 89 mu and 195 bu. Each mu is calculated to yield 4 dou of rice.
The official also requires the farmer to pay 3 hu of grain, where 1 hu of grain is equivalent to 4 dou of rice.
Question: What is the total amount of rice and grain?

The procedure says: Place the number of mu of the field. Multiply it by 240 bu, then add 195 bu, obtaining 21555 bu as the total.
Divide this by the lower field's hu divisor, 600 bu, to get the amount of rice.
To find the grain, multiply 3 hu by the amount of rice, obtaining 107 hu, 7 dou, 7 sheng, and 5 ge as the total.
Divide this by 1 hu = 4 dou to get the amount of grain. If there is a remainder, convert it into fractional parts.

How do we know the lower field's divisor is 600 bu? The procedure says: Place 240 bu and divide it by 4 dou of rice, obtaining 60 bu as the divisor for 1 dou. Multiply this by 10 to get 600 bu, which is the divisor for 1 hu.

To know how much rice is produced per bu of the lower field, calculate 1 he and 2/3 he per bu. The procedure says: Place 4 dou of rice, multiply it by 10 twice to get 400 he. Divide this by 240 bu, obtaining 1 he and 2/3 he per bu.

Answer: *a* hu of rice, *b* hu of grain.
"""

from fractions import Fraction

# 下官田八十九畞一百九十五步
田畞數 = 89
田步數 = 195

# 每畞二百四十步
每畞步數 = 240

# 置田畞數，以二百四十步乘之，內一百九十五步
總步數 = (田畞數 * 每畞步數) + 田步數

# 下田斛法六百步
下田斛法 = 600

# 以下田斛法六百步除之，得米數
米數 = Fraction(總步數, 下田斛法)

# 官亦令納榖三斛，準米一斛四斗
榖比率 = 3  # 3 hu of grain per rice
米比率 = 4  # 1 hu = 4 dou of rice

# 以三斛因米，得 107 斛 7 斗 7 升 5 合為實
榖實 = 米數 * 榖比率

# 以一斛四斗除，為穀數
穀數 = Fraction(榖實, 米比率)

# 答曰米 a 斛，穀 b 斛
a = 米數
b = 穀數#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 4311/56, Actual: 4311/160"""
