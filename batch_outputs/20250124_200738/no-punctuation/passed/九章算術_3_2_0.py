"""
今有甲持錢五百六十乙持錢三百五十丙持錢一百八十凡三人俱出關關稅百錢欲以錢數多少衰出之問各幾何
術曰各置錢數為列衰副并為法以百錢乘未并者各自為實實如法得一錢
荅曰甲出 a錢 乙出 b錢 丙出 c錢 
"""

#----- content starts here -----
"""
Suppose there are three people: Jia holds 560 qian, Yi holds 350 qian, and Bing holds 180 qian.
In total, the three people pass through a checkpoint, and the checkpoint tax is 100 qian.
It is desired to divide the tax in proportion to the amount of money each person holds.

The procedure says: Place the amounts of money held by each person in a line.
In auxiliary, add them together to form the divisor.
Multiply the checkpoint tax by the amounts not yet added together, forming the dividend for each person.
Do the division, obtaining the amount of tax each person pays.

The answer says: Jia pays *a* qian, Yi pays *b* qian, Bing pays *c* qian.
"""

# 甲持錢五百六十
甲錢 = 560

# 乙持錢三百五十
乙錢 = 350

# 丙持錢一百八十
丙錢 = 180

# 關稅百錢
關稅 = 100

# 各置錢數為列
錢數 = [甲錢, 乙錢, 丙錢]

# 衰副并為法
法 = sum(錢數)

# 以百錢乘未并者，各自為實
實 = [關稅 * i for i in 錢數]

# 實如法得一錢
a, b, c = [Fraction(i, 法) for i in 實]#----- content ends here -----

"""
"""
