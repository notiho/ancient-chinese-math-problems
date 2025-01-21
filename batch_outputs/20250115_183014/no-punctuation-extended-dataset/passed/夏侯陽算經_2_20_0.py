"""
今有兩稅米一千五百七十八斛九斗送州每斗腳一十三文竝於身内抽充時估斗别一百三十文問正及腳各幾何
術曰置米數以毎石一百三十文乗之為實又置一百三十文加腳一十三文得一百四十三文為法除得正米數欲求腳米數以毎斗一十三文乗稅數為實以一百四十三文為法除之即腳數
答曰正米 a斛 腳米 b斛
"""

"""
Suppose there are 1578 hu and 9 dou of tax rice to be delivered to the prefecture. 
For every dou, the transportation cost (footing) is 13 wen. 
The market price for each dou is 130 wen. 
Question: how much rice is for the actual tax (principal) and how much is for the footing (transportation cost)?

The procedure says: Place the total rice amount. Multiply it by 130 wen per shi to obtain the dividend.
Also, place 130 wen and add 13 wen for footing, obtaining 143 wen as the divisor. Divide to get the principal rice amount.
To find the footing rice amount, multiply 13 wen per dou by the total rice amount to obtain the dividend. Divide by 143 wen as the divisor to get the footing rice amount.

Answer: the principal rice is *a* hu, and the footing rice is *b* hu.
"""

from fractions import Fraction

# 兩稅米一千五百七十八斛九斗
稅米 = 1578 + Fraction(9, 10)

# 每石一百三十文
每石價 = 130

# 每斗腳一十三文
每斗腳 = 13

# 每石價加腳，得一百四十三文
法 = 每石價 + 每斗腳

# 正米計算
# 置米數以每石一百三十文乘之，為實
正實 = 每石價 * 稅米

# 除以法，得正米數
正米 = Fraction(正實, 法)

# 腳米計算
# 以每斗一十三文乘稅數，為實
腳實 = 每斗腳 * 稅米

# 除以法，得腳米數
腳米 = Fraction(腳實, 法)

a = 正米
b = 腳米
"""
"""
