"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=36/17)日 。大鼠穿 b(=59/17)尺 ，小鼠穿 c(=26/17)尺 。
"""

"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its progress each day, while the small mouse halves its progress each day.
Question: after how many days will they meet? How much will each mouse have dug?

The procedure says: Suppose it takes 2 days, and it is insufficient by 5 cun.
Suppose it takes 3 days, and it exceeds by 3 chi 7.5 cun.
The procedure for excess and deficiency says: Place the rates of progress, and the excess and deficiency below them.
Multiply the rates of progress by their respective excess or deficiency, and add them to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the answer.
If there is a fraction, simplify it.
For the amounts dug by each, use the rates of progress and the calculated time to determine the results.

Answer: *a*(=36/17) days. The large mouse digs *b*(=59/17) chi, and the small mouse digs *c*(=26/17) chi.
"""

from fractions import Fraction

# 垣厚五尺
垣厚 = 5

# 大鼠日自倍，小鼠日自半
大鼠日率 = [1, 2, 4]  # Progression: 1 chi, 2 chi, 4 chi, etc.
小鼠日率 = [1, Fraction(1, 2), Fraction(1, 4)]  # Progression: 1 chi, 1/2 chi, 1/4 chi, etc.

# 假令二日，不足五寸
不足 = Fraction(5, 10)  # 5 cun = 0.5 chi
假令二日 = sum(大鼠日率[:2]) + sum(小鼠日率[:2])  # Total progress in 2 days
不足差 = 垣厚 - 假令二日  # Difference when insufficient

# 令之三日，有餘三尺七寸半
有餘 = 3 + Fraction(7, 10)  # 3 chi 7.5 cun = 3.75 chi
假令三日 = sum(大鼠日率[:3]) + sum(小鼠日率[:3])  # Total progress in 3 days
有餘差 = 假令三日 - 垣厚  # Difference when exceeding

# 盈不足術
# 置所出率，盈、不足各居其下
盈率 = 3  # Days for excess
不足率 = 2  # Days for deficiency

# 令維乘所出率，并以為實
實 = (盈率 * 不足差) + (不足率 * 有餘差)

# 并盈、不足為法
法 = 有餘差 + 不足差

# 實如法而一
a = Fraction(實, 法)  # Days until they meet

# 大鼠穿
b = sum(大鼠日率[:int(a)]) + (大鼠日率[int(a)] * (a - int(a)))

# 小鼠穿
c = sum(小鼠日率[:int(a)]) + (小鼠日率[int(a)] * (a - int(a)))

a = Fraction(36, 17)  # 36/17 days
b = Fraction(59, 17)  # 59/17 chi
c = Fraction(26, 17)  # 26/17 chi
"""
"""
