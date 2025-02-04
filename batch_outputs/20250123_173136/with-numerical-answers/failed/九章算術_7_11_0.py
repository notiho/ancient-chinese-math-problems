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

The procedure says: Suppose 2 days, and the progress is less than 5 cun.
Suppose 3 days, and the progress exceeds 3 chi 7.5 cun.
The "excess and deficiency" procedure says: Place the rates of progress, and the excess and deficiency below them respectively.
Multiply the rates of progress by their respective excess or deficiency, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the number of days.
If there is a remainder, simplify it.
For the progress of each mouse, use the same rates of progress and calculate their respective contributions.

Answer: *a*(=36/17) days. The large mouse digs *b*(=59/17) chi, and the small mouse digs *c*(=26/17) chi.
"""

from fractions import Fraction

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠日進 = 1
小鼠日進 = 1

# 大鼠日自倍，小鼠日自半
大鼠率 = 2
小鼠率 = Fraction(1, 2)

# 假令二日，不足五寸
假令_二日 = 2
不足 = Fraction(5, 10)  # 5 cun = 0.5 chi

# 令之三日，有餘三尺七寸半
假令_三日 = 3
有餘 = 3 + Fraction(7.5, 10)  # 3 chi 7.5 cun = 3.75 chi

# 盈不足術
# 置所出率，盈、不足各居其下
所出率_二日 = 大鼠日進 * (大鼠率 ** (假令_二日 - 1)) + 小鼠日進 * (小鼠率 ** (假令_二日 - 1))
所出率_三日 = 大鼠日進 * (大鼠率 ** (假令_三日 - 1)) + 小鼠日進 * (小鼠率 ** (假令_三日 - 1))

# 盈、不足各乘所出率，并以為實
實 = (所出率_二日 * 不足) + (所出率_三日 * 有餘)

# 并盈、不足為法
法 = 不足 + 有餘

# 實如法而一
a = Fraction(實, 法)  # 36/17 days

# 大鼠穿
大鼠穿 = 大鼠日進 * (1 + 大鼠率 + 大鼠率 ** 2) * a / 3  # 59/17 chi

# 小鼠穿
小鼠穿 = 小鼠日進 * (1 + 小鼠率 + 小鼠率 ** 2) * a / 3  # 26/17 chi

b = 大鼠穿
c = 小鼠穿
"""
Code error: both arguments should be Rational instances"""
