"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a日 。大鼠穿 b尺 ，小鼠穿 c尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its progress each day, while the small mouse halves its progress each day.
Question: how many days will it take for them to meet? How much will each mouse dig?

The procedure says: Suppose 2 days, and the progress is less than 5 cun. Suppose 3 days, and the progress exceeds 3 chi 7.5 cun.
The "excess and deficiency" procedure says: Place the rates of progress, and the excess and deficiency below them respectively. Multiply the rates of progress by the respective excess or deficiency, and sum them to form the dividend. Sum the excess and deficiency to form the divisor. Divide the dividend by the divisor to find the number of days. If there is a fraction, simplify it. To find how much each mouse digs, use the rates of progress and calculate accordingly.

Answer: *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

from fractions import Fraction

# Wall thickness
垣厚 = 5  # chi

# Rates of progress
大鼠日進 = 1  # chi/day
小鼠日進 = 1  # chi/day

# Progression rules
大鼠倍增 = lambda day: 大鼠日進 * (2 ** (day - 1))  # Large mouse doubles its progress each day
小鼠減半 = lambda day: 小鼠日進 * (1 / (2 ** (day - 1)))  # Small mouse halves its progress each day

# Assume 2 days: calculate total progress
大鼠2日 = 大鼠倍增(1) + 大鼠倍增(2)
小鼠2日 = 小鼠減半(1) + 小鼠減半(2)
總進度2日 = 大鼠2日 + 小鼠2日
不足 = 垣厚 - 總進度2日  # Deficiency

# Assume 3 days: calculate total progress
大鼠3日 = 大鼠倍增(1) + 大鼠倍增(2) + 大鼠倍增(3)
小鼠3日 = 小鼠減半(1) + 小鼠減半(2) + 小鼠減半(3)
總進度3日 = 大鼠3日 + 小鼠3日
盈餘 = 總進度3日 - 垣厚  # Excess

# 盈不足術 calculation
盈 = 盈餘
不足 = 不足
大鼠率 = 大鼠日進
小鼠率 = 小鼠日進

# Dividend (實)
實 = (盈 * 大鼠率) + (不足 * 小鼠率)

# Divisor (法)
法 = 盈 + 不足

# Days to meet
a = Fraction(實, 法)

# Calculate how much each mouse digs
b = 大鼠倍增(1) + 大鼠倍增(2) + 大鼠倍增(3)  # Large mouse's total progress
c = 垣厚 - b  # Small mouse's total progress

# Final answer
a日 = a
b尺 = b
c尺 = c

a日, b尺, c尺#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
