"""
今有兩稅米一千五百七十八斛九斗送州每斗腳一十三文竝於身内抽充時估斗别一百三十文問正及腳各幾何
術曰置米數以毎石一百三十文乗之為實又置一百三十文加腳一十三文得一百四十三文為法除得正米數欲求腳米數以毎斗一十三文乗稅數為實以一百四十三文為法除之即腳數
答曰正米 a斛 腳米 b斛
"""

"""
Suppose there are 1578 hu and 9 dou of tax rice to be delivered to the prefecture. 
Each dou incurs a transportation fee of 13 wen. 
At the same time, the estimated value of each dou is 130 wen. 
Question: how much rice is for the actual tax (zheng) and how much is for the transportation fee (jiao)?

The procedure says: Place the amount of rice. Multiply it by 130 wen per shi to obtain the dividend.
Also place 130 wen and add 13 wen for the transportation fee, obtaining 143 wen as the divisor.
Divide to obtain the amount of zheng rice.
To find the amount of jiao rice, multiply the tax rice by 13 wen per dou to obtain the dividend.
Use 143 wen as the divisor and divide to obtain the amount of jiao rice.

Answer: *a* hu of zheng rice, *b* hu of jiao rice.
"""

from fractions import Fraction

# 米數
米數 = 1578 + Fraction(9, 10)  # 1578斛9斗 (1斛 = 10斗)

# 每石一百三十文
每石價值 = 130

# 每斗腳一十三文
每斗腳 = 13

# 置米數，以每石一百三十文乘之，為實
正實 = 米數 * 每石價值

# 置一百三十文，加腳一十三文，得一百四十三文，為法
法 = 每石價值 + 每斗腳

# 除得正米數
a = Fraction(正實, 法)

# 欲求腳米數，以每斗一十三文乘稅數，為實
腳實 = 米數 * 每斗腳

# 以一百四十三文為法除之，即腳數
b = Fraction(腳實, 法)
"""
"""
