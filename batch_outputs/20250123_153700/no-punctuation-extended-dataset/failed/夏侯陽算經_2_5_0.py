"""
今有下官田八十九畞一百九十五步畞别計米四斗輸官官亦令納榖三斛準米一斛四斗問合計米及穀幾何
術曰置田畞數以二百四十步乗之内一百九十五步得二萬一千五百五十五步為實以下田斛法六百步除之得米數欲求穀者以三斛因米得一百七斛七斗七升五合為實以一斛四斗除為穀數不盡者命分何以知下田六百步為法術曰置二百四十步以米四斗為法除得六十步為一斗之法上十之為六百步乃為一斛之法欲知下田一步計米一合三分合之二術曰置米四斗再上十之為四百合為實以二百四十步除之得一合不盡者與法俱八約之命分
答曰米 a斛 穀 b斛
"""

"""
Suppose there is a lower official's field of 89 mu and 195 bu. Each mu yields 4 dou of rice.
The official also requires the payment of 3 hu of grain, with the conversion rate being 1 hu = 4 dou of rice.
Question: What is the total amount of rice and grain?

The procedure says:
1. Place the number of mu of the field. Multiply it by 240 bu, then add the remaining 195 bu. This gives the total number of bu as the dividend.
2. Divide this by the lower field's hu divisor, 600 bu, to obtain the amount of rice.
3. To find the amount of grain, multiply 3 hu by the amount of rice, obtaining the dividend. Divide this by 1 hu = 4 dou to obtain the amount of grain.
4. If there is a remainder, express it as a fraction.

How do we know the lower field's divisor is 600 bu? The procedure says:
- Place 240 bu and divide it by 4 dou of rice, obtaining 60 bu per dou. Multiply this by 10 to get 600 bu, which is the divisor for 1 hu.

To calculate how much rice corresponds to 1 bu of the lower field:
- Place 4 dou of rice, multiply it by 10 to get 400 ge (1 dou = 100 ge). Divide this by 240 bu, obtaining 1 ge per bu. If there is a remainder, express it as a fraction.

Answer: The total is *a* hu of rice and *b* hu of grain.
"""

from fractions import Fraction

# 下官田八十九畞一百九十五步
田畞數 = 89
田步數 = 195

# 每畞二百四十步
每畞步 = 240

# 計算田的總步數
總步數 = (田畞數 * 每畞步) + 田步數

# 下田斛法六百步
下田斛法 = 600

# 以下田斛法六百步除之，得米數
米數 = Fraction(總步數, 下田斛法)

# 官令納榖三斛，準米一斛四斗
榖比率 = 3  # 每米數對應的榖數
每斛斗 = 4  # 一斛等於四斗

# 以三斛因米得為實
榖實 = 榖比率 * 米數

# 以一斛四斗除，為穀數
穀數 = Fraction(榖實, 每斛斗)

# 答案
a = 米數
b = 穀數
"""
Variable 'b' has wrong value. Expected: 4311/56, Actual: 4311/160"""
