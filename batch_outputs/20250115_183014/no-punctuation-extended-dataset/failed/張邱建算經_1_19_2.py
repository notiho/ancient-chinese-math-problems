"""
今有鐵十斤一經入爐得七斤今有鐵三經入爐得七十九斤一十一兩問未入爐本鐵㡬何
術曰置鐵三經入爐得斤兩數以十斤再自乗乃乗上為實以七斤再自乗為法實如法而得一
答曰 a斤
"""

"""
Suppose there is 10 jin of iron. After being smelted once in the furnace, it becomes 7 jin.
Now suppose there is iron that has been smelted three times in the furnace, resulting in 79 jin and 11 liang.
Question: how much iron was there originally before smelting?

The procedure says: Place the weight of the iron after three smeltings (in jin and liang).
Take 10 jin, square it, and multiply it by the weight after three smeltings to form the dividend.
Take 7 jin, square it, to form the divisor.
Divide the dividend by the divisor to obtain the original weight of the iron.

Answer: *a* jin.
"""

# 鐵十斤一經入爐得七斤
初鐵 = 10
一經鐵 = 7

# 鐵三經入爐得七十九斤一十一兩
三經鐵 = 79 + Fraction(11, 16)  # 1 jin = 16 liang

# 以十斤再自乘
初鐵平方 = 初鐵 ** 2

# 乃乘上為實
實 = 初鐵平方 * 三經鐵

# 以七斤再自乘為法
一經鐵平方 = 一經鐵 ** 2
法 = 一經鐵平方

# 實如法而得一
a = Fraction(實, 法)  # Original weight of the iron before smelting
"""
Variable 'a' has wrong value. Expected: 159375/686, Actual: 31875/196"""
