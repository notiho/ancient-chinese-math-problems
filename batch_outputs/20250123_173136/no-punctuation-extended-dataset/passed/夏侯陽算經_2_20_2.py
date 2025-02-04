"""
今有兩稅米一千五百七十八斛九斗送州每斗腳一十三文竝於身内抽充時估斗别一百三十文問正及腳各幾何
術曰置米數以毎石一百三十文乗之為實又置一百三十文加腳一十三文得一百四十三文為法除得正米數欲求腳米數以毎斗一十三文乗稅數為實以一百四十三文為法除之即腳數
答曰正米 a斛 腳米 b斛
"""

"""
Suppose there are 1578 hu and 9 dou of tax rice to be delivered to the prefecture. 
For every dou, the transport fee (jiaojiao) is 13 wen. 
The estimated value of each dou of rice is 130 wen. 
Question: how much rice is for the actual tax (zhengmi), and how much is for the transport fee (jiaomi)?

The procedure says: Place the total amount of rice. 
Multiply it by 130 wen per shi to obtain the dividend. 
Also, place 130 wen and add the transport fee of 13 wen, obtaining 143 wen as the divisor. 
Divide, obtaining the amount of actual tax rice. 
To find the transport fee rice, multiply 13 wen per dou by the total rice amount to obtain the dividend. 
Divide by 143 wen as the divisor, obtaining the transport fee rice.

Answer: the actual tax rice is *a* hu, and the transport fee rice is *b* hu.
"""

from fractions import Fraction

# 兩稅米一千五百七十八斛九斗
稅米 = 1578 + Fraction(9, 10)

# 每石一百三十文
每石估價 = 130

# 每斗腳一十三文
每斗腳 = 13

# 置米數以每石一百三十文乘之為實
正米實 = 稅米 * 每石估價

# 置一百三十文加腳一十三文得一百四十三文為法
法 = 每石估價 + 每斗腳

# 除得正米數
a = Fraction(正米實, 法)

# 欲求腳米數以每斗一十三文乘稅數為實
腳米實 = 稅米 * 每斗腳

# 以一百四十三文為法除之即腳數
b = Fraction(腳米實, 法)
"""
"""
