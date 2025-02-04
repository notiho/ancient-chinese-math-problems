"""
今有上官田七十四畝一百五十三步畞别計米六斗輸官官令納穀三斛準米一斛四斗問米及穀各幾何
術曰置畞數以二百四十步乗之内餘步得一萬七千九百一十三步為實以上田斛法四百步除之得米數欲求穀者以三斛因米為一百三十四斛三斗四升七合五勺以米一斛四斗除之欲知上田一斛計步數者置田一畞二百四十步以米六斗為法除得四十步計米一斗以斗法上十之為四百步即斛法上田一步計米二合五勺欲知者置米六斗再上十之以二百四十步除之見毎步之數
答曰米 a斛 穀 b斛
"""

"""
Suppose there is a field of 74 mu and 153 bu. For each mu, 6 dou of rice are calculated. The officials require 3 hu of grain for every 1 hu and 4 dou of rice.
Question: how much rice and grain are required?

The procedure says:
1. Place the number of mu, multiply it by 240 bu, and add the remaining bu. This gives the total number of bu as the dividend.
2. Divide this by the upper-field hu divisor, 400 bu, to obtain the amount of rice.
3. To find the amount of grain, take 3 hu as equivalent to 134 hu, 3 dou, 4 sheng, 7 ge, and 5 jue. Divide this by 1 hu and 4 dou of rice.
4. To know how many bu correspond to 1 hu in the upper field, place 1 mu (240 bu) and divide it by 6 dou of rice. This gives 40 bu per dou. Multiply this by 10 to get 400 bu per hu.
5. To calculate how much rice corresponds to 1 bu, place 6 dou of rice, multiply it by 10, and divide by 240 bu. This gives the amount of rice per bu.

Answer: *a* hu of rice, *b* hu of grain.
"""

from fractions import Fraction

# 上官田七十四畝一百五十三步
畝數 = 74
餘步 = 153

# 畞别計米六斗
每畝米 = 6  # 斗

# 輸官官令納穀三斛準米一斛四斗
穀對米 = Fraction(3)  # 穀對應米的比例
米對穀 = Fraction(1, 3)  # 米對應穀的比例
米一斛 = 10  # 1斛 = 10斗
米一斛四斗 = 米一斛 + 4  # 1斛4斗 = 14斗

# Step 1: 計算總步數
# 置畞數以二百四十步乘之，內餘步
總步數 = 畝數 * 240 + 餘步  # 總步數

# Step 2: 計算米數
# 以上田斛法四百步除之，得米數
上田斛法 = 400  # 每斛對應的步數
米數 = Fraction(總步數, 上田斛法)  # 得到米數（斛）

# Step 3: 計算穀數
# 欲求穀者以三斛因米為一百三十四斛三斗四升七合五勺
穀數 = 米數 * 穀對米  # 穀數（斛）

# 答案
a = 米數
b = 穀數
"""
Variable 'b' has wrong value. Expected: 7677/80, Actual: 53739/400"""
