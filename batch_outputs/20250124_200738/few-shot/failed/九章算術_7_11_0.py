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
Question: after how many days do they meet? How much does each mouse dig?

The procedure says: Suppose for 2 days, the progress is insufficient by 5 cun. Suppose for 3 days, the progress exceeds by 3 chi 7.5 cun.
The "Excess and Deficit" procedure says: Place the rates of progress under the respective excess and deficit. Multiply the rates by the respective days and combine them to form the dividend. Combine the excess and deficit to form the divisor. Divide the dividend by the divisor to find the number of days. If there is a remainder, simplify it. For the progress of each mouse, use the rates of progress, subtract the smaller from the larger, and simplify the result.

Answer: *a* days. The large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

from fractions import Fraction

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠初速 = 1
小鼠初速 = 1

# 大鼠日自倍，小鼠日自半
大鼠二日速 = 大鼠初速 * 2
小鼠二日速 = 小鼠初速 / 2

# 假令二日，不足五寸
不足 = Fraction(5, 10)  # 5 cun = 0.5 chi

# 令之三日，有餘三尺七寸半
有餘 = 3 + Fraction(7.5, 10)  # 3 chi 7.5 cun = 3.75 chi

# 盈不足術
# 置所出率
大鼠二日進 = 大鼠初速 + 大鼠二日速
小鼠二日進 = 小鼠初速 + 小鼠二日速

# 盈、不足各居其下
不足率 = 大鼠二日進 + 小鼠二日進
有餘率 = 大鼠二日進 * 1.5 + 小鼠二日進 * 1.5

# 令維乘所出率，并以為實
實 = (不足 * 有餘率) + (有餘 * 不足率)

# 并盈、不足為法
法 = 有餘 - 不足#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
