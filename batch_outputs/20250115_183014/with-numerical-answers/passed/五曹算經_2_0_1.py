"""
今有丁二萬三千六百九十二人，責兵五千九百二十三人。問：㡬何丁出一兵？
術曰：列二萬三千六百九十二人，以五千九百二十三除之即得。
答曰： a(=4) 丁出 b(=1) 兵。
"""

"""
Suppose there are 23,692 adult males (丁), and 5,923 soldiers are required.
Question: how many adult males are needed to provide one soldier?

The procedure says: Place 23,692 adult males, and divide it by 5,923. The result is obtained.

Answer: *a*(=4) adult males provide *b*(=1) soldier.
"""

# 列二萬三千六百九十二人
丁 = 23692

# 以五千九百二十三除之即得
兵 = 5923

# 丁出兵比例
比例 = Fraction(丁, 兵)

a = 比例.numerator  # 4 丁
b = 比例.denominator  # 1 兵
"""
"""
