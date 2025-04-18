"""
今有三女，長女五日一歸，中女四日一歸，少女三日一歸。問：三女幾何日相會？
術曰：置長女五日，中女四日，少女三日，于右方，各列一算于左方，維乘之，各得所到數。長女十二到，中女十五到，少女二十到，又各以歸日乘到數，即得。
答曰： a日 。
"""

#----- content starts here -----

# 長女五日一歸
長女 = 5

# 中女四日一歸
中女 = 4

# 少女三日一歸
少女 = 3

# 各列一算于左方，維乘之，各得所到數
長女到數 = 中女 * 少女  # 4 * 3 = 12
中女到數 = 長女 * 少女  # 5 * 3 = 15
少女到數 = 長女 * 中女  # 5 * 4 = 20

# 又各以歸日乘到數，即得
長女積 = 長女 * 長女到數  # 5 * 12
中女積 = 中女 * 中女到數  # 4 * 15
少女積 = 少女 * 少女到數  # 3 * 20

# 求總和
總和 = 長女積 + 中女積 + 少女積

# 求歸日乘積的公倍數
公倍數 = 長女到數 + 中女到數 + 少女到數

# 答曰：a日
a = Fraction(總和, 公倍數)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60, Actual: 180/47"""
