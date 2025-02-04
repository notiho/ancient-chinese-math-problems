"""
今有上官田七十四畝一百五十三步畞别計米六斗輸官官令納穀三斛準米一斛四斗問米及穀各幾何
術曰置畞數以二百四十步乗之内餘步得一萬七千九百一十三步為實以上田斛法四百步除之得米數欲求穀者以三斛因米為一百三十四斛三斗四升七合五勺以米一斛四斗除之欲知上田一斛計步數者置田一畞二百四十步以米六斗為法除得四十步計米一斗以斗法上十之為四百步即斛法上田一步計米二合五勺欲知者置米六斗再上十之以二百四十步除之見毎步之數
答曰米 a斛 穀 b斛
"""

#----- content starts here -----
"""
Suppose there is Shangguan land of 74 mu and 153 bu. For each mu, 6 dou of rice is calculated. The officials require 3 hu of grain, where 1 hu is equivalent to 4 dou of rice.
Question: how much rice and grain are there respectively?

The procedure says: Place the number of mu, multiply it by 240 bu, and add the remaining bu. This gives 17913 bu as the total. Divide this by the Shangguan hu divisor of 400 bu, obtaining the amount of rice.
To find the grain, take 3 hu as equivalent to 134 hu, 3 dou, 4 sheng, 7 ge, and 5 jue. Divide this by 1 hu of 4 dou to find the grain.
To know the number of bu per hu for Shangguan land, place 240 bu per mu and divide by 6 dou of rice, obtaining 40 bu per dou. Multiply by 10 to get 400 bu per hu.
To find the amount of rice per bu, place 6 dou of rice, multiply by 10, and divide by 240 bu to find the amount per bu.

Answer: *a* hu of rice, *b* hu of grain.
"""

from fractions import Fraction

# 上官田七十四畝一百五十三步
畝數 = 74
餘步 = 153

# 畞别計米六斗
每畝米 = 6  # 斗

# 輸官官令納穀三斛準米一斛四斗
穀斛 = 3
米斛 = 1
米斗 = 4

# 置畞數以二百四十步乘之，內餘步
每畝步 = 240
總步數 = (畝數 * 每畝步) + 餘步  # 得 17913 步

# 以上田斛法四百步除之，得米數
上田斛法 = 400
米數 = Fraction(總步數, 上田斛法)  # 斛

# 欲求穀者以三斛因米為一百三十四斛三斗四升七合五勺
穀數 = 米數 * Fraction(穀斛, 米斛 + Fraction(米斗, 10))  # 斛

# 答曰米 a斛 穀 b斛
a = 米數
b = 穀數#----- content ends here -----

"""
"""
