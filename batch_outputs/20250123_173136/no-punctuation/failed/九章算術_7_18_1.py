"""
今有良馬與駑馬發長安至齊齊去長安三千里良馬初日行一百九十三里日增十三里駑馬初日行九十七里日減半里良馬先至齊復還迎駑馬問幾何日相逢及各行幾何
術曰假令十五日不足三百三十七里半令之十六日多一百四十里以盈不足維乘假令之數并而為實并盈不足為法實如法而一得日數不盡者以等數除之而命分
荅曰 a日 而相逢良馬行 b里 駑馬行 c里 
"""

"""
Suppose there are two horses, a good horse and a slow horse, departing from Chang'an to Qi.
The distance from Chang'an to Qi is 3000 li.
The good horse travels 193 li on the first day, increasing its distance by 13 li each day.
The slow horse travels 97 li on the first day, decreasing its distance by 0.5 li each day.
The good horse reaches Qi first, then returns to meet the slow horse.
Question: How many days until they meet, and how far does each horse travel?

The procedure says: Assume 15 days, which is insufficient by 337.5 li.
Assume 16 days, which is excessive by 140 li.
Multiply the assumed days by the insufficiency and add them to form the dividend.
Add the insufficiency and excess to form the divisor.
Divide the dividend by the divisor to get the number of days.
If there is a remainder, divide it by the difference in daily rates to get the fractional part.

Answer: *a* days until they meet, the good horse travels *b* li, and the slow horse travels *c* li.
"""

# 齊去長安三千里
總距離 = 3000

# 良馬初日行一百九十三里，日增十三里
良馬初日 = 193
良馬日增 = 13

# 駑馬初日行九十七里，日減半里
駑馬初日 = 97
駑馬日減 = Fraction(1, 2)

# 假令十五日
假令_15日 = 15

# 良馬 15 日行的距離
良馬_15日距離 = sum(良馬初日 + i * 良馬日增 for i in range(假令_15日))

# 駑馬 15 日行的距離
駑馬_15日距離 = sum(駑馬初日 - i * 駑馬日減 for i in range(假令_15日))

# 15 日不足的距離
不足距離 = 總距離 - (良馬_15日距離 + 駑馬_15日距離)

# 假令十六日
假令_16日 = 16

# 良馬 16 日行的距離
良馬_16日距離 = sum(良馬初日 + i * 艉馬日增 for i in range(假令_16日))

# 駑馬 16 日行的距離
駑馬_16日距離 = sum(駑馬初日 - i * 駑馬日減 for i in range(假令_16日))

# 16 日多出的距離
多出距離 = (良馬_16日距離 + 駑馬_16日距離) - 總距離

# 維乘假令之數并而為實
實 = (假令_15日 * 多出距離) + (假令_16日 * 不足距離)

# 并盈不足為法
法 = 多出距離 + 不足距離

# 實如法而一得日數
a = Fraction(實, 法)

# 計算良馬與駑馬的總行程
良馬行程 = sum(良馬初日 + i * 良馬日增 for i in range(int(a)))
駑馬行程 = sum(駑馬初日 - i * 駑馬日減 for i in range(int(a)))

b = 良馬行程
c = 駑馬行程
"""
Code error: name '艉馬日增' is not defined"""
