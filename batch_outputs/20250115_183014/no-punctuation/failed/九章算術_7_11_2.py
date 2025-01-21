"""
今有垣厚五尺兩鼠對穿大鼠日一尺小鼠亦日一尺大鼠日自倍小鼠日自半問幾何日相逢各穿幾何
術曰假令二日不足五寸令之三日有餘三尺七寸半
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數荅曰 a日 大鼠穿 b尺 小鼠穿 c尺 
"""

"""
Suppose there is a wall 5 chi thick. Two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its daily progress each day, while the small mouse halves its daily progress each day.
Question: after how many days will they meet, and how much will each mouse dig?

The procedure says: Suppose 2 days are insufficient by 5 cun. Assume 3 days exceed by 3 chi 7 cun and a half.
Using the "excess and deficiency" method:
Place the rates of progress for the excess and deficiency under their respective values.
Multiply the rates of progress by their respective values, and sum them to form the dividend.
Sum the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the number of days.
If there is a remainder, convert it to the same unit.
If the excess and deficiency are consistent, use the same method to calculate the total progress of each mouse.

Answer: *a* days, the large mouse digs *b* chi, and the small mouse digs *c* chi.
"""

# 垣厚五尺
垣厚 = 5

# 假令二日不足五寸
不足日數 = 2
不足量 = Fraction(5, 10)  # 5 寸 = 5/10 尺

# 令之三日有餘三尺七寸半
有餘日數 = 3
有餘量 = 3 + Fraction(7, 10) + Fraction(5, 20)  # 3 尺 7 寸半 = 3 + 7/10 + 5/20 尺

# 盈不足術
# 置所出率盈不足各居其下
不足率 = 2  # 大鼠和小鼠日進度差異
有餘率 = 3  # 大鼠和小鼠日進度差異

# 令維乘所出率并以為實
實 = (不足率 * 有餘量) + (有餘率 * 不足量)

# 并盈不足為法
法 = 不足率 + 有餘率

# 實如法而一
a = Fraction(實, 法)

# 大鼠穿 b 尺
b = 1 + 2 * (a - 1)

# 小鼠穿 c 尺
c = 1 + Fraction(1, 2) * (a - 1)  # 小鼠日自半

# Output the results
a日 = a
b尺 = b
c尺 = c
"""
Variable 'a' has wrong value. Expected: 36/17, Actual: 47/25
Variable 'b' has wrong value. Expected: 59/17, Actual: 69/25
Variable 'c' has wrong value. Expected: 26/17, Actual: 36/25"""
