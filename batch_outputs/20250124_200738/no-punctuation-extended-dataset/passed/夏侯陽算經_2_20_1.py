"""
今有兩稅米一千五百七十八斛九斗送州每斗腳一十三文竝於身内抽充時估斗别一百三十文問正及腳各幾何
術曰置米數以毎石一百三十文乗之為實又置一百三十文加腳一十三文得一百四十三文為法除得正米數欲求腳米數以毎斗一十三文乗稅數為實以一百四十三文為法除之即腳數
答曰正米 a斛 腳米 b斛
"""

#----- content starts here -----
"""
Suppose there are 1578 hu and 9 dou of tax rice to be delivered to the prefecture.
For each dou, the transportation fee (jiaojiao) is 13 wen.
The current market price for rice is 130 wen per dou.
Question: how much rice is used for the actual tax (zhengmi), and how much is used for the transportation fee (jiaomi)?

The procedure says:
1. Place the total amount of rice and multiply it by 130 wen per dou to obtain the dividend.
2. Add the transportation fee of 13 wen to 130 wen, obtaining 143 wen as the divisor.
3. Divide the dividend by the divisor to obtain the amount of tax rice (zhengmi).
4. To find the transportation rice (jiaomi), multiply the total rice by 13 wen per dou to obtain the dividend.
5. Divide this by 143 wen to obtain the amount of transportation rice (jiaomi).

Answer: the tax rice is *a* hu, and the transportation rice is *b* hu.
"""

from fractions import Fraction

# 兩稅米一千五百七十八斛九斗
稅米 = 1578 + Fraction(9, 10)  # Convert 9 dou to hu (1 hu = 10 dou)

# 每斗時估一百三十文
時估 = 130

# 每斗腳一十三文
腳費 = 13

# 置米數以每石一百三十文乘之，為實
實正 = 稅米 * 時估

# 置一百三十文加腳一十三文，得一百四十三文為法
法 = 時估 + 腳費

# 除得正米數
正米 = Fraction(實正, 法)

# 欲求腳米數，以每斗一十三文乘稅數，為實
實腳 = 稅米 * 腳費

# 以一百四十三文為法除之，即腳數
腳米 = Fraction(實腳, 法)

a = 正米
b = 腳米#----- content ends here -----

"""
"""
