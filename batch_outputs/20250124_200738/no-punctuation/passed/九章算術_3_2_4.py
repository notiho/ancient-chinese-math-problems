"""
今有甲持錢五百六十乙持錢三百五十丙持錢一百八十凡三人俱出關關稅百錢欲以錢數多少衰出之問各幾何
術曰各置錢數為列衰副并為法以百錢乘未并者各自為實實如法得一錢
荅曰甲出 a錢 乙出 b錢 丙出 c錢 
"""

#----- content starts here -----
"""
Suppose there are three people: Jia holds 560 qian, Yi holds 350 qian, and Bing holds 180 qian.
In total, the three people are crossing a checkpoint, and the checkpoint tax is 100 qian.
It is desired to divide the tax proportionally according to the amount of money each person holds.

The procedure says: Place the amounts of money in a line.
Each of them becomes on its own an [element in the] decreasing sequence.
In auxiliary, add them, giving the divisor.
Multiply the [numbers] that have not been added together by the 100 qian.
Each of them becomes on its own a dividend.
Do the division, obtaining the amount of qian each person pays.

The answer says: Jia pays *a* qian, Yi pays *b* qian, and Bing pays *c* qian.
"""

# 甲持錢五百六十
甲 = 560

# 乙持錢三百五十
乙 = 350

# 丙持錢一百八十
丙 = 180

# 關稅百錢
關稅 = 100

# 各置錢數為列
錢數 = [甲, 乙, 丙]

# 衰副并為法
法 = sum(錢數)

# 以百錢乘未并者
實 = [關稅 * i for i in 錢數]

# 各自為實，實如法得一錢
a, b, c = [Fraction(i, 法) for i in 實]#----- content ends here -----

"""
"""
