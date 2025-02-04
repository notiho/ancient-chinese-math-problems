"""
今有下官田八十九畞一百九十五步畞别計米四斗輸官官亦令納榖三斛準米一斛四斗問合計米及穀幾何
術曰置田畞數以二百四十步乗之内一百九十五步得二萬一千五百五十五步為實以下田斛法六百步除之得米數欲求穀者以三斛因米得一百七斛七斗七升五合為實以一斛四斗除為穀數不盡者命分何以知下田六百步為法術曰置二百四十步以米四斗為法除得六十步為一斗之法上十之為六百步乃為一斛之法欲知下田一步計米一合三分合之二術曰置米四斗再上十之為四百合為實以二百四十步除之得一合不盡者與法俱八約之命分
答曰米 a斛 穀 b斛
"""

"""
Suppose there is a lower official's field of 89 mu and 195 bu. Each mu yields 4 dou of rice.
The official also requires the payment of 3 hu of grain, with 1 hu of grain equivalent to 4 dou of rice.
Question: What is the total amount of rice and grain?

The procedure says:
1. Place the number of mu of the field. Multiply it by 240 bu, then add 195 bu, obtaining 21555 bu as the total.
2. Divide this by the lower field's hu divisor of 600 bu, obtaining the amount of rice.
3. To find the grain, multiply 3 hu by the amount of rice, obtaining 107 hu, 7 dou, 7 sheng, and 5 ge as the total.
4. Divide this by 1 hu (4 dou), obtaining the amount of grain. If there is a remainder, convert it into fractional parts.

How do we know the lower field's divisor is 600 bu for 1 hu?
The procedure says:
- Place 240 bu. Divide it by 4 dou of rice, obtaining 60 bu as the divisor for 1 dou.
- Multiply this by 10, obtaining 600 bu as the divisor for 1 hu.

How do we know 1 bu of the lower field yields 1/240 dou of rice?
The procedure says:
- Place 4 dou of rice. Multiply it by 10 twice, obtaining 400 ge as the total.
- Divide this by 240 bu, obtaining 1 ge. If there is a remainder, convert it into fractional parts.

Answer: *a* hu of rice, *b* hu of grain.
"""

from fractions import Fraction

# 下官田八十九畞一百九十五步
田畞數 = 89
田步數 = 195

# 畞别計米四斗
每畞米 = 4  # 斗

# 官亦令納榖三斛準米一斛四斗
榖比米 = 3  # 榖比米的倍數
一斛米 = 4  # 斗

# 置田畞數，以二百四十步乘之，內一百九十五步
總步數 = 田畞數 * 240 + 田步數  # 總步數 = 21555

# 以下田斛法六百步除之，得米數
下田斛法 = 600  # 每斛的步數
米數 = Fraction(總步數, 下田斛法)  # 得米數 (斛)

# 欲求穀者，以三斛因米
穀實 = 榖比米 * 米數  # 穀的實數 (斛)

# 以一斛四斗除，為穀數
穀數 = 穀實  # 穀數 (斛)

# 答
a = 米數  # 米數 (斛)
b = 穀數  # 穀數 (斛)
"""
Variable 'b' has wrong value. Expected: 4311/56, Actual: 4311/40"""
