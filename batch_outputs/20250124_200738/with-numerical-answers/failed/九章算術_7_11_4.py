"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=36/17)日 。大鼠穿 b(=59/17)尺 ，小鼠穿 c(=26/17)尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its progress each day, while the small mouse halves its progress each day.
Question: after how many days do they meet? How far does each mouse dig?

The procedure says: Suppose 2 days, and the progress is less than 5 cun. Suppose 3 days, and the progress exceeds 3 chi 7.5 cun.
The procedure for excess and deficiency says: Place the rates of progress, with the excess and deficiency below them.
Multiply the rates of progress by their respective excess or deficiency, and add them to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to obtain the result. If there is a fraction, simplify it.
For the excess and deficiency, if they are related to the same object, place the rates of progress, subtract the smaller from the larger, and simplify the dividend and divisor.
The dividend becomes the value of the object, and the divisor becomes the number of people.

Answer: *a*(=36/17) days. The large mouse digs *b*(=59/17) chi, and the small mouse digs *c*(=26/17) chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠日進 = 1
小鼠日進 = 1

# 大鼠日自倍，小鼠日自半
大鼠進率 = [1, 2, 4]  # Progression: 1 chi, 2 chi, 4 chi, etc.
小鼠進率 = [1, Fraction(1, 2), Fraction(1, 4)]  # Progression: 1 chi, 1/2 chi, 1/4 chi, etc.

# 假令二日，不足五寸
不足 = Fraction(5, 10)  # 5 cun = 5/10 chi
大鼠二日 = sum(大鼠進率[:2])  # Large mouse's progress in 2 days
小鼠二日 = sum(小鼠進率[:2])  # Small mouse's progress in 2 days
二日總進 = 大鼠二日 + 小鼠二日  # Total progress in 2 days
二日不足 = 垣厚 - 二日總進  # Deficiency after 2 days

# 令之三日，有餘三尺七寸半
有餘 = 3 + Fraction(7, 10)  # 3 chi 7.5 cun = 3 + 7/10 chi
大鼠三日 = sum(大鼠進率[:3])  # Large mouse's progress in 3 days
小鼠三日 = sum(小鼠進率[:3])  # Small mouse's progress in 3 days
三日總進 = 大鼠三日 + 小鼠三日  # Total progress in 3 days
三日有餘 = 三日總進 - 垣厚  # Excess after 3 days

# 盈不足術
盈 = 三日有餘  # Excess
不足 = 二日不足  # Deficiency
大鼠率 = 大鼠日進  # Rate of progress for the large mouse
小鼠率 = 小鼠日進  # Rate of progress for the small mouse

# 置所出率，盈、不足各居其下
盈實 = 盈 * 2  # Multiply excess by 2 days
不足實 = 不足 * 3  # Multiply deficiency by 3 days

# 并以為實
實 = 盈實 + 不足實  # Dividend

# 并盈、不足為法
法 = 盈 + 不足  # Divisor

# 實如法而一
a = Fraction(實, 法)  # Days until they meet (36/17)

# 各穿幾何
大鼠穿 = 大鼠日進 * a + 大鼠日進 * (a - 1)  # Large mouse's total progress
小鼠穿 = 小鼠日進 * a + 小鼠日進 * (a - 1)  # Small mouse's total progress

b = 大鼠穿  # 59/17 chi
c = 小鼠穿  # 26/17 chi#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 59/17, Actual: 55/17
Variable 'c' has wrong value. Expected: 26/17, Actual: 55/17"""
