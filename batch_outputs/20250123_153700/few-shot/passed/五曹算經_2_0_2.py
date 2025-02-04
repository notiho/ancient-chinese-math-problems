"""
今有丁二萬三千六百九十二人，責兵五千九百二十三人。問：㡬何丁出一兵？
術曰：列二萬三千六百九十二人，以五千九百二十三除之即得。
答曰： a 丁出一兵。
"""

"""
Suppose there are 23,692 adult males (丁), and 5,923 soldiers are required.
Question: how many adult males are needed to provide one soldier?

The procedure says: Place 23,692 adult males and divide it by 5,923 to obtain the result.

Answer: *a* adult males provide one soldier.
"""

# 列二萬三千六百九十二人
丁 = 23692

# 以五千九百二十三除之即得
兵 = 5923

# 計算每兵所需丁數
a = Fraction(丁, 兵)
"""
"""
