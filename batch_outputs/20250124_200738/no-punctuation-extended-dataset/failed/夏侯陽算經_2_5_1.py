"""
今有下官田八十九畞一百九十五步畞别計米四斗輸官官亦令納榖三斛準米一斛四斗問合計米及穀幾何
術曰置田畞數以二百四十步乗之内一百九十五步得二萬一千五百五十五步為實以下田斛法六百步除之得米數欲求穀者以三斛因米得一百七斛七斗七升五合為實以一斛四斗除為穀數不盡者命分何以知下田六百步為法術曰置二百四十步以米四斗為法除得六十步為一斗之法上十之為六百步乃為一斛之法欲知下田一步計米一合三分合之二術曰置米四斗再上十之為四百合為實以二百四十步除之得一合不盡者與法俱八約之命分
答曰米 a斛 穀 b斛
"""

#----- content starts here -----
"""
Suppose there is a field of 89 mu and 195 bu. For each mu, 4 dou of rice is calculated. The officials also require 3 hu of grain, with 1 hu equivalent to 4 dou of rice.
Question: What is the total amount of rice and grain?

The procedure says: Place the number of mu of the field, multiply it by 240 bu, and add the remaining 195 bu. This gives the total number of bu. Use the lower field hu divisor of 600 bu to divide it, obtaining the amount of rice. 
To find the amount of grain, multiply 3 hu by the amount of rice, giving the total grain. Divide this by 1 hu (4 dou) to obtain the amount of grain. If there is a remainder, express it as a fraction.

To verify the lower field divisor of 600 bu: Place 240 bu, divide it by 4 dou of rice, obtaining 60 bu as the divisor for 1 dou. Multiply it by 10, obtaining 600 bu as the divisor for 1 hu.

To verify the calculation of rice per bu: Place 4 dou of rice, multiply it by 10 twice, obtaining 400 ge. Divide this by 240 bu, obtaining 1 ge per bu. If there is a remainder, express it as a fraction.

Answer: *a* hu of rice, *b* hu of grain.
"""

from fractions import Fraction

# 田八十九畞一百九十五步
畞數 = 89
步數 = 195

# 每畞二百四十步
每畞步數 = 240

# 置田畞數以二百四十步乘之，內一百九十五步
總步數 = 畞數 * 每畞步數 + 步數

# 下田斛法六百步
下田斛法 = 600

# 以下田斛法六百步除之，得米數
米數 = Fraction(總步數, 下田斛法)

# 官亦令納榖三斛
榖比率 = 3

# 以三斛因米，得榖實
榖實 = 榖比率 * 米數

# 一斛四斗
一斛斗數 = 4

# 以一斛四斗除，為穀數
穀數 = Fraction(榖實, 一斛斗數)

# 答案
a = 米數
b = 穀數#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 4311/56, Actual: 4311/160"""
