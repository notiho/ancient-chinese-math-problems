"""
今有上官田七十四畝一百五十三步畞别計米六斗輸官官令納穀三斛準米一斛四斗問米及穀各幾何
術曰置畞數以二百四十步乗之内餘步得一萬七千九百一十三步為實以上田斛法四百步除之得米數欲求穀者以三斛因米為一百三十四斛三斗四升七合五勺以米一斛四斗除之欲知上田一斛計步數者置田一畞二百四十步以米六斗為法除得四十步計米一斗以斗法上十之為四百步即斛法上田一步計米二合五勺欲知者置米六斗再上十之以二百四十步除之見毎步之數
答曰米 a斛 穀 b斛
"""

"""
Suppose there is a field of 74 mu and 153 bu. For each mu, 6 dou of rice are calculated. The officials require 3 hu of grain to be paid, where 1 hu of grain is equivalent to 4 dou of rice.
Question: how much rice and grain are there respectively?

The procedure says:
1. Place the number of mu and multiply it by 240 bu, then add the remaining bu, obtaining 17913 bu as the total.
2. Use the official field grain standard of 400 bu per hu to divide it, obtaining the amount of rice.
3. To find the amount of grain, consider that 3 hu of grain are equivalent to 134 hu, 3 dou, 4 sheng, 7 ge, and 5 jue of rice. Divide this by 1 hu of rice being equivalent to 4 dou.
4. To know how many bu per hu of rice for the official field, place 240 bu per mu and divide by 6 dou, obtaining 40 bu per dou. Multiply this by 10 to get 400 bu per hu.
5. To know how much rice per bu, place 6 dou of rice, multiply by 10, and divide by 240 bu, obtaining the amount of rice per bu.

Answer: *a* hu of rice, *b* hu of grain.
"""

from fractions import Fraction

# 上官田七十四畝一百五十三步
畝數 = 74
餘步 = 153

# 每畝二百四十步
每畝步數 = 240

# 置畞數以二百四十步乘之，內餘步
總步數 = 畝數 * 每畝步數 + 餘步  # 得 17913 步

# 上田斛法四百步
斛法 = 400

# 除之，得米數
米數 = Fraction(總步數, 斛法)

# 官令納穀三斛，準米一斛四斗
米每斛斗數 = 4

# 穀數 = 米數 / 米每斛斗數
穀數 = Fraction(米數, 米每斛斗數)

# 答案
a = 米數
b = 穀數
"""
Variable 'b' has wrong value. Expected: 7677/80, Actual: 17913/1600"""
