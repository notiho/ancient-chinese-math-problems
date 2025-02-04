"""
今有兩稅米一千五百七十八斛九斗送州每斗腳一十三文竝於身内抽充時估斗别一百三十文問正及腳各幾何
術曰置米數以毎石一百三十文乗之為實又置一百三十文加腳一十三文得一百四十三文為法除得正米數欲求腳米數以毎斗一十三文乗稅數為實以一百四十三文為法除之即腳數
答曰正米 a斛 腳米 b斛
"""

#----- content starts here -----
"""
Suppose there are 1578 hu and 9 dou of tax rice to be delivered to the prefecture. 
For each dou, the transport fee (jiaojiao) is 13 wen. 
The market price at the time is 130 wen per dou.
Question: how much rice is allocated for the actual tax (zhengmi) and how much for the transport fee (jiaomi)?

The procedure says: Place the amount of rice. Multiply it by 130 wen per shi to obtain the dividend.
Also place 130 wen, add the transport fee of 13 wen, obtaining 143 wen as the divisor. Divide to obtain the amount of actual tax rice.
To seek the amount of transport fee rice, multiply the tax rice by 13 wen per dou to obtain the dividend. Divide by 143 wen as the divisor to obtain the amount of transport fee rice.

Answer: the actual tax rice is *a* hu, and the transport fee rice is *b* hu.
"""

from fractions import Fraction

# 兩稅米一千五百七十八斛九斗
稅米 = 1578 + Fraction(9, 10)  # Convert 9 dou to hu (1 hu = 10 dou)

# 每石一百三十文
每石價格 = 130

# 每斗腳一十三文
每斗腳 = 13

# 置米數以每石一百三十文乘之，為實
實 = 稅米 * 每石價格

# 又置一百三十文，加腳一十三文，得一百四十三文，為法
法 = 每石價格 + 每斗腳

# 除得正米數
正米 = Fraction(實, 法)

# 欲求腳米數，以每斗一十三文乘稅數，為實
腳實 = 稅米 * 每斗腳

# 以一百四十三文為法除之，即腳數
腳米 = Fraction(腳實, 法)

a = 正米
b = 腳米#----- content ends here -----

"""
"""
