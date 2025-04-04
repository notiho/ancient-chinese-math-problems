"""
今有鐵十斤一經入爐得七斤今有鐵三經入爐得七十九斤一十一兩問未入爐本鐵㡬何
術曰置鐵三經入爐得斤兩數以十斤再自乗乃乗上為實以七斤再自乗為法實如法而得一
答曰 a斤
"""

#----- content starts here -----
"""
Suppose there are 10 jin of iron. After being smelted once in the furnace, it becomes 7 jin.
Now, suppose there is iron that has been smelted three times in the furnace, resulting in 79 jin and 11 liang.
Question: how much iron was there originally before smelting?

The procedure says: Place the weight of the iron after being smelted three times in jin and liang.
Take 10 jin, square it, and multiply it by the weight after three smeltings to obtain the dividend.
Take 7 jin, square it, to obtain the divisor.
Divide the dividend by the divisor to find the original weight.

Answer: *a* jin.
"""

# 鐵十斤一經入爐得七斤
初始鐵 = 10
一經鐵 = 7

# 鐵三經入爐得七十九斤一十一兩
三經鐵_斤 = 79
三經鐵_兩 = 11

# 轉換兩為斤 (16兩 = 1斤)
三經鐵 = 三經鐵_斤 + Fraction(三經鐵_兩, 16)

# 以十斤再自乘乃乘上為實
實 = (初始鐵 ** 2) * 三經鐵

# 以七斤再自乘為法
法 = 一經鐵 ** 2

# 實如法而得一
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 159375/686, Actual: 31875/196"""
