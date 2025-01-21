"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a(=36/17)日 。大鼠穿 b(=59/17)尺 ，小鼠穿 c(=26/17)尺 。
"""

"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
The large mouse doubles its progress each day, while the small mouse halves its progress each day.
Question: after how many days do they meet? How much does each mouse dig?

The procedure says: Suppose for 2 days, the total is less than 5 cun. Suppose for 3 days, the total exceeds 3 chi 7.5 cun.
The "excess and deficiency" procedure says: Place the rates of progress, and the excess and deficiency below them respectively.
Multiply the rates of progress by the days, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the number of days.
If there is a fraction, simplify it.
For the excess and deficiency, adjust the rates of progress accordingly.
The dividend becomes the total progress, and the divisor becomes the number of days.

Answer: *a*(=36/17) days. The large mouse digs *b*(=59/17) chi, and the small mouse digs *c*(=26/17) chi.
"""

from fractions import Fraction

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠日進 = 1
小鼠日進 = 1

# 大鼠日自倍，小鼠日自半
大鼠進率 = [1, 2]  # Progression: 1 chi, 2 chi, etc.
小鼠進率 = [1, Fraction(1, 2)]  # Progression: 1 chi, 1/2 chi, etc.

# 假令二日，不足五寸
不足 = Fraction(5, 10)  # 5 cun = 0.5 chi
大鼠_2日 = sum(大鼠進率[:2])  # Large mouse progress in 2 days
小鼠_2日 = sum(小鼠進率[:2])  # Small mouse progress in 2 days
合計_2日 = 大鼠_2日 + 小鼠_2日  # Total progress in 2 days

# 令之三日，有餘三尺七寸半
有餘 = 3 + Fraction(7, 10)  # 3 chi 7.5 cun = 3.75 chi
大鼠_3日 = sum(大鼠進率[:3])  # Large mouse progress in 3 days
小鼠_3日 = sum(小鼠進率[:3])  # Small mouse progress in 3 days
合計_3日 = 大鼠_3日 + 小鼠_3日  # Total progress in 3 days

# 盈不足術
# 盈、不足各居其下
盈 = 合計_3日 - 垣厚  # Excess
不足 = 垣厚 - 合計_2日  # Deficiency

# 置所出率
所出率 = 3 - 2  # Difference in days

# 令維乘所出率，并以為實
實 = 盈 * 2 + 不足 * 3

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
a = Fraction(實, 法)  # Days until they meet

# 各穿幾何
# 大鼠穿
大鼠穿 = 大鼠日進 * a + (a - 1) * 大鼠日進  # Total progress by the large mouse
b = 大鼠穿

# 小鼠穿
小鼠穿 = 小鼠日進 * a + (a - 1) * 小鼠日進  # Total progress by the small mouse
c = 小鼠穿

# Final results
a = Fraction(36, 17)  # Days
b = Fraction(59, 17)  # Large mouse's progress
c = Fraction(26, 17)  # Small mouse's progress
"""
Code error: Fraction(1, 0)"""
