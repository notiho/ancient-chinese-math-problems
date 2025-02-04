"""
今有丁二萬三千六百九十二人責兵五千九百二十三人問㡬何丁出一兵
術曰列二萬三千六百九十二人以五千九百二十三除之即得
答曰 a 丁出一兵
"""

"""
Suppose there are 23,692 adult males (丁), and 5,923 soldiers are required.
Question: how many adult males are needed to provide one soldier?

The procedure says: Arrange 23,692 adult males and divide it by 5,923. The result is obtained.

Answer: *a* adult males provide one soldier.
"""

# 列二萬三千六百九十二人
丁 = 23692

# 以五千九百二十三除之
兵 = 5923

# 即得
a = Fraction(丁, 兵)
"""
"""
