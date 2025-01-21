"""
今有上官田七十四畝一百五十三步畞别計米六斗輸官官令納穀三斛準米一斛四斗問米及穀各幾何
術曰置畞數以二百四十步乗之内餘步得一萬七千九百一十三步為實以上田斛法四百步除之得米數欲求穀者以三斛因米為一百三十四斛三斗四升七合五勺以米一斛四斗除之欲知上田一斛計步數者置田一畞二百四十步以米六斗為法除得四十步計米一斗以斗法上十之為四百步即斛法上田一步計米二合五勺欲知者置米六斗再上十之以二百四十步除之見毎步之數
答曰米 a斛 穀 b斛
"""

"""
Suppose there is a field of 74 mu and 153 bu. For each mu, 6 dou of rice are calculated. The officials require 3 hu of grain for every 1 hu and 4 dou of rice.
Question: how much rice and grain are there respectively?

The procedure says:
1. Place the number of mu and multiply it by 240 bu. Add the remaining bu to get the total number of bu, which is 17913 bu.
2. Use the upper-field rice divisor of 400 bu to divide it, obtaining the amount of rice.
3. To find the amount of grain, take 3 hu as equivalent to 134 hu, 3 dou, 4 sheng, 7 ge, and 5 jue. Divide this by 1 hu and 4 dou of rice.
4. To calculate the number of bu per hu of rice in the upper field, place 240 bu per mu and divide it by 6 dou of rice, obtaining 40 bu per dou. Multiply this by 10 to get 400 bu per hu, which is the rice divisor for the upper field.
5. To find the amount of rice per bu, place 6 dou of rice, multiply it by 10, and divide it by 240 bu to find the amount of rice per bu.

Answer: *a* hu of rice, *b* hu of grain.
"""

from fractions import Fraction

# 上官田七十四畝一百五十三步
畝數 = 74
餘步 = 153

# 每畝二百四十步
每畝步數 = 240

# 置畞數以二百四十步乘之，內餘步
總步數 = (畝數 * 每畝步數) + 餘步  # 得 17913 步

# 上田斛法四百步
上田斛法 = 400

# 以上田斛法四百步除之，得米數
米數 = Fraction(總步數, 上田斛法)

# 官令納穀三斛準米一斛四斗
米斛 = 1
米斗 = 4
穀斛 = 3

# 計米一斛四斗為多少穀
穀當量 = (穀斛 * 10) + 米斗  # 穀當量為 34 斗

# 穀數 = 米數 * 穀當量 / (米斛 * 10 + 米斗)
穀數 = 米數 * 穀當量 / ((米斛 * 10) + 米斗)

a = 米數
b = 穀數
"""
Variable 'b' has wrong value. Expected: 7677/80, Actual: 43503/400"""
