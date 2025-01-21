"""
今有垣厚五尺兩鼠對穿大鼠日一尺小鼠亦日一尺大鼠日自倍小鼠日自半問幾何日相逢各穿幾何
術曰假令二日不足五寸令之三日有餘三尺七寸半
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰 a日 大鼠穿 b尺 小鼠穿 c尺 
"""

"""
Suppose there is a wall 5 chi thick. Two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its daily progress each day, while the small mouse halves its daily progress each day.
Question: after how many days will they meet, and how much will each mouse have dug?

The procedure says: Suppose that in 2 days, the total progress is less than 5 cun (insufficient). Then, suppose in 3 days, the total progress exceeds 3 chi 7 cun and a half.
Using the "excess and deficiency" method:
Place the rates of progress for each day under the respective "excess" and "deficiency" values.
Multiply the rates of progress by their respective values and add them together to form the dividend.
Add the "excess" and "deficiency" values together to form the divisor.
Divide the dividend by the divisor to find the number of days. If there is a remainder, convert it to a fraction.
If the "excess" and "deficiency" are the same, use the rates of progress to adjust the calculation.
The result gives the number of days, and the progress of each mouse can then be calculated.

Answer: *a* days, the large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

from fractions import Fraction

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠初速 = 1
小鼠初速 = 1

# 大鼠日自倍，小鼠日自半
大鼠速率 = [大鼠初速 * (2 ** i) for i in range(10)]  # Precompute rates for 10 days
小鼠速率 = [小鼠初速 * (1 / (2 ** i)) for i in range(10)]  # Precompute rates for 10 days

# 假令二日不足五寸
不足進度 = sum(大鼠速率[:2]) + sum(小鼠速率[:2])  # Progress in 2 days
不足 = 垣厚 - 不足進度

# 令之三日有餘三尺七寸半
有餘進度 = sum(大鼠速率[:3]) + sum(小鼠速率[:3])  # Progress in 3 days
有餘 = 有餘進度 - 垣厚

# 盈不足術
# 置所出率盈不足各居其下
盈不足率 = [2, 3]  # Days corresponding to "insufficient" and "excess"

# 令維乘所出率并以為實
實 = (盈不足率[0] * 有餘) + (盈不足率[1] * 不足)

# 并盈不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)  # Number of days

# 計算大鼠和小鼠各自穿的距離
大鼠穿 = sum(大鼠速率[:int(a)]) + (a - int(a)) * 大鼠速率[int(a)]
小鼠穿 = sum(小鼠速率[:int(a)]) + (a - int(a)) * 小鼠速率[int(a)]

b = 大鼠穿
c = 小鼠穿
"""
Code error: both arguments should be Rational instances"""
