"""
今有垣厚五尺，兩鼠對穿。大鼠日一尺，小鼠亦日一尺。大鼠日自倍，小鼠日自半。問︰幾何日相逢？各穿幾何？
術曰：假令二日，不足五寸。令之三日，有餘三尺七寸半。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰： a(=36/17)日 。大鼠穿 b(=59/17)尺 ，小鼠穿 c(=26/17)尺 。
"""

"""
Suppose there is a wall 5 chi thick, and two mice are digging through it from opposite sides.
The large mouse digs 1 chi per day, and the small mouse also digs 1 chi per day.
However, the large mouse doubles its progress each day, while the small mouse halves its progress each day.
Question: after how many days will they meet? How much will each mouse have dug?

The procedure says: Suppose for 2 days, the progress is insufficient by 5 cun. Suppose for 3 days, the progress exceeds by 3 chi and 7.5 cun.
The "Excess and Deficiency" procedure says: Place the rates of progress, and the excess and deficiency below them, respectively.
Multiply the rates of progress by the respective excess and deficiency, and sum them to obtain the dividend.
Sum the excess and deficiency to obtain the divisor.
Divide the dividend by the divisor to obtain the result. If there is a fraction, simplify it.
For the amounts dug by each mouse, use the same rates of progress, subtract the smaller from the larger, and simplify the result.
The dividend becomes the total amount dug, and the divisor becomes the number of days.

Answer: *a*(=36/17) days. The large mouse digs *b*(=59/17) chi, and the small mouse digs *c*(=26/17) chi.
"""

# 垣厚五尺
垣厚 = 5

# 大鼠日一尺，小鼠亦日一尺
大鼠日進 = 1
小鼠日進 = 1

# 大鼠日自倍，小鼠日自半
大鼠進率 = [1, 2]  # Progression: 1 chi, 2 chi, ...
小鼠進率 = [1, Fraction(1, 2)]  # Progression: 1 chi, 1/2 chi, ...

# 假令二日，不足五寸
不足 = Fraction(5, 10)  # 5 cun = 5/10 chi

# 令之三日，有餘三尺七寸半
有餘 = 3 + Fraction(7.5, 10)  # 3 chi 7.5 cun = 3 + 7.5/10 chi

# 盈不足術
# 置所出率，盈、不足各居其下
大鼠進率_二日 = 大鼠進率[0] + 大鼠進率[1]  # 1 + 2 = 3 chi in 2 days
小鼠進率_二日 = 小鼠進率[0] + 小鼠進率[1]  # 1 + 1/2 = 3/2 chi in 2 days
二日總進 = 大鼠進率_二日 + 小鼠進率_二日  # Total progress in 2 days

大鼠進率_三日 = 大鼠進率_二日 + 4  # Add 4 chi for the 3rd day (doubles again)
小鼠進率_三日 = 小鼠進率_二日 + Fraction(1, 4)  # Add 1/4 chi for the 3rd day (halves again)
三日總進 = 大鼠進率_三日 + 小鼠進率_三日  # Total progress in 3 days

# 令維乘所出率，并以為實
實 = (三日總進 * 不足) + (二日總進 * 有餘)

# 并盈、不足為法
法 = 有餘 + 不足

# 實如法而一
a = Fraction(實, 法)  # Days until they meet

# 大鼠穿
大鼠穿 = 大鼠日進 * a + 大鼠日進 * (a - 1)  # Total distance dug by the large mouse

# 小鼠穿
小鼠穿 = 小鼠日進 * a
"""
Code error: both arguments should be Rational instances"""
