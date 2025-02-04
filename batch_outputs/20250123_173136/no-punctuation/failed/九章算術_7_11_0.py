"""
今有垣厚五尺兩鼠對穿大鼠日一尺小鼠亦日一尺大鼠日自倍小鼠日自半問幾何日相逢各穿幾何
術曰假令二日不足五寸令之三日有餘三尺七寸半
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a日 大鼠穿 b尺 小鼠穿 c尺 
"""

"""
Suppose there is a wall 5 chi thick. Two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its daily progress, while the small mouse halves its daily progress.
Question: after how many days do they meet, and how much has each mouse dug?

The procedure says:
Assume for 2 days, the progress is less than 5 cun. Assume for 3 days, the progress exceeds 3 chi 7.5 cun.
Using the "excess and deficiency" method:
Place the rates of progress for each assumption under their respective results (excess and deficiency).
Multiply the rates of progress by their respective results, and sum them to obtain the dividend.
Sum the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to obtain the number of days. If there is a remainder, simplify it.
For the progress of each mouse, multiply the number of days by their respective rates of progress.

Answer: *a* days, the large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

from fractions import Fraction

# 垣厚五尺
垣厚 = 5

# 大鼠日自倍，小鼠日自半
大鼠日率 = 2
小鼠日率 = Fraction(1, 2)

# 假令二日不足五寸
假令_二日 = 2
不足 = Fraction(5, 10)  # 5 cun = 0.5 chi

# 假令三日有餘三尺七寸半
假令_三日 = 3
有餘 = 3 + Fraction(7.5, 10)  # 3 chi 7.5 cun = 3.75 chi

# 盈不足術
# 置所出率盈不足各居其下
所出率_二日 = 假令_二日 * 大鼠日率 + 假令_二日 * 小鼠日率
所出率_三日 = 假令_三日 * 大鼠日率 + 假令_三日 * 小鼠日率

# 盈不足相與同
盈 = 有餘
不足 = 垣厚 - 不足

# 維乘所出率并以為實
實 = (所出率_二日 * 盈) + (所出率_三日 * 不足)

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
a = Fraction(實, 法)

# 大鼠穿 b 尺
b = a * 大鼠日率

# 小鼠穿 c 尺
c = a * 小鼠日率
"""
Code error: both arguments should be Rational instances"""
