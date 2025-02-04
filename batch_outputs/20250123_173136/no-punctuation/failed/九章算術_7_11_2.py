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
Question: after how many days do they meet, and how far has each mouse dug?

The procedure says: Suppose 2 days are insufficient by 5 cun. Assume 3 days exceed by 3 chi 7 cun and 5 fen.
Using the "Excess and Deficiency" method:
Place the rates of progress for the excess and deficiency below each case.
Multiply the rates of progress by the respective excess or deficiency, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
If the excess and deficiency are the same, use the rates of progress to determine the result.
For the final calculation, place the rates of progress, subtract the smaller from the larger, and simplify the divisor and dividend.

Answer: *a* days, the large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日自倍，小鼠日自半
大鼠日進 = 2
小鼠日進 = Fraction(1, 2)

# 假令二日不足五寸
不足 = Fraction(5, 10)  # 5 cun = 0.5 chi

# 令之三日有餘三尺七寸半
有餘 = 3 + Fraction(7, 10) + Fraction(5, 100)  # 3 chi 7 cun 5 fen = 3.75 chi

# 盈不足術
# 置所出率盈不足各居其下
大鼠率 = 2
小鼠率 = Fraction(1, 2)

# 令維乘所出率并以為實
實 = (大鼠率 * 有餘) + (小鼠率 * 不足)

# 并盈不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)

# 大鼠穿 b 尺
b = 大鼠日進 * a

# 小鼠穿 c 尺
c = 小鼠日進 * a
"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 31/17
Variable 'b' has wrong value. Expected: 59/17, Actual: 62/17
Variable 'c' has wrong value. Expected: 26/17, Actual: 31/34"""
