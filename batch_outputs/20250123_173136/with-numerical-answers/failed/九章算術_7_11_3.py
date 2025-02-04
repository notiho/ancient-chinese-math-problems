"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=36/17)日 。大鼠穿 b(=59/17)尺 ，小鼠穿 c(=26/17)尺 。
"""

"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
The large mouse doubles its progress each day, while the small mouse halves its progress each day.
Question: after how many days do they meet? How much does each mouse dig?

The procedure says: Suppose 2 days, and it is insufficient by 5 cun. Suppose 3 days, and there is an excess of 3 chi 7.5 cun.
The "excess and deficiency" procedure says: Place the rates of progress, with the excess and deficiency below each rate.
Multiply the rates by their respective excess or deficiency, and add them to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to get the result. If there is a fraction, simplify it.
For the amounts dug by the mice, use the rates of progress, subtract the smaller from the larger, and simplify the result using the divisor and dividend.
The dividend becomes the amount dug, and the divisor becomes the number of days.

Answer: *a*(=36/17) days. The large mouse digs *b*(=59/17) chi, and the small mouse digs *c*(=26/17) chi.
"""

from fractions import Fraction

# 垣厚五尺
垣厚 = 5

# 假令二日，不足五寸
不足日數 = 2
不足量 = Fraction(5, 10)  # 5 寸 = 5/10 尺

# 令之三日，有餘三尺七寸半
有餘日數 = 3
有餘量 = 3 + Fraction(7.5, 10)  # 3 尺 7 寸半 = 3 + 7.5/10 尺

# 盈不足術曰：置所出率，盈、不足各居其下
不足實 = 有餘日數 * 不足量
有餘實 = 不足日數 * 有餘量

# 并以為實
實 = 不足實 + 有餘實

# 并盈、不足為法
法 = 不足量 + 有餘量

# 實如法而一
a = Fraction(實, 法)  # 36/17 days

# 大鼠日自倍，小鼠日自半
大鼠日率 = 1 + 1  # 每日進度
小鼠日率 = 1 / 2 + 1 / 4  # 每日進度

# 大鼠穿
b = 大鼠日率 * a  # 59/17 尺

# 小鼠穿
c = 小鼠日率 * a  # 26/17 尺
"""
Code error: both arguments should be Rational instances"""
