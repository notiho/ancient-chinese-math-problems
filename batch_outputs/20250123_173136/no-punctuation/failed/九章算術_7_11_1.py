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
Assume that in 2 days, the progress is insufficient by 5 cun (0.5 chi). Assume that in 3 days, the progress exceeds by 3 chi 7 cun 5 fen (3.75 chi).
Using the "Excess and Deficiency" method:
Place the rates of progress for the two cases, and place the excess and deficiency below them.
Multiply the rates of progress by their respective excess or deficiency, and sum these to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the number of days. If there is a remainder, simplify it.
If the excess and deficiency are equal, the result is valid.
For the price of the goods, place the rates of progress, subtract the smaller from the larger, and simplify the divisor and dividend.

Answer: *a* days, the large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日自倍，小鼠日自半
大鼠日進 = 2
小鼠日進 = Fraction(1, 2)

# 假令二日不足五寸 (0.5 尺)
假令二日進 = 2 * 大鼠日進 + 2 * 小鼠日進
不足 = 垣厚 - 假令二日進

# 假令三日有餘三尺七寸半 (3.75 尺)
假令三日進 = 3 * 大鼠日進 + 3 * 小鼠日進
有餘 = 假令三日進 - 垣厚

# 盈不足術
# 置所出率盈不足各居其下
所出率 = [2, 3]
盈不足 = [不足, 有餘]

# 令維乘所出率并以為實
實 = 所出率[0] * 盈不足[1] + 所出率[1] * 盈不足[0]

# 并盈不足為法
法 = 盈不足[0] + 盈不足[1]

# 實如法而一
a = Fraction(實, 法)

# 大鼠穿 b 尺
b = a * 大鼠日進

# 小鼠穿 c 尺
c = a * 小鼠日進
"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 2
Variable 'b' has wrong value. Expected: 59/17, Actual: 4
Variable 'c' has wrong value. Expected: 26/17, Actual: 1"""
