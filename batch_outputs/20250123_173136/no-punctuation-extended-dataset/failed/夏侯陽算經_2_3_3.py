"""
今有上官田七十四畝一百五十三步畞别計米六斗輸官官令納穀三斛準米一斛四斗問米及穀各幾何
術曰置畞數以二百四十步乗之内餘步得一萬七千九百一十三步為實以上田斛法四百步除之得米數欲求穀者以三斛因米為一百三十四斛三斗四升七合五勺以米一斛四斗除之欲知上田一斛計步數者置田一畞二百四十步以米六斗為法除得四十步計米一斗以斗法上十之為四百步即斛法上田一步計米二合五勺欲知者置米六斗再上十之以二百四十步除之見毎步之數
答曰米 a斛 穀 b斛
"""

"""
Suppose there is a field of 74 mu and 153 bu. Each mu is calculated to yield 6 dou of rice. 
The officials require 3 hu of grain to be paid, where 1 hu of grain is equivalent to 4 dou of rice. 
Question: how much rice and grain are there respectively?

The procedure says: Place the number of mu and multiply it by 240 bu, adding the remaining bu, to obtain 17913 bu as the total.
Using the upper field hu divisor of 400 bu, divide it to obtain the amount of rice.
To calculate the grain, treat 3 hu as 134 hu 3 dou 4 sheng 7 ge 5 jue, and divide it by 1 hu (4 dou of rice).
To know how many bu correspond to 1 hu in the upper field, place 1 mu (240 bu) and divide it by 6 dou of rice, obtaining 40 bu per dou.
Multiply it by 10 to get 400 bu per hu, which is the hu divisor for the upper field.
To calculate how much rice corresponds to 1 bu, place 6 dou of rice, multiply it by 10, and divide it by 240 bu, obtaining the amount of rice per bu.

Answer: *a* hu of rice, *b* hu of grain.
"""

# 上官田七十四畝一百五十三步
畝數 = 74
餘步 = 153

# 每畝二百四十步
畝步 = 240

# 置畞數以二百四十步乘之，內餘步
總步數 = 畝數 * 畝步 + 餘步

# 上田斛法四百步
斛法 = 400

# 以上田斛法四百步除之，得米數
米數 = Fraction(總步數, 斛法)

# 官令納穀三斛，準米一斛四斗
穀斛 = 3
米斛斗 = 4

# 穀數 = 穀斛 * 米斛斗
穀數 = 穀斛 * 米斛斗

# 答曰米 a斛 穀 b斛
a = 米數
b = 穀數
"""
Variable 'b' has wrong value. Expected: 7677/80, Actual: 12"""
