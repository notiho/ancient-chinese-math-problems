"""
今有良馬與駑馬發長安至齊齊去長安三千里良馬初日行一百九十三里日增十三里駑馬初日行九十七里日減半里良馬先至齊復還迎駑馬問幾何日相逢及各行幾何
術曰假令十五日不足三百三十七里半令之十六日多一百四十里以盈不足維乘假令之數并而為實并盈不足為法實如法而一得日數不盡者以等數除之而命分
荅曰 a日 而相逢良馬行 b里 駑馬行 c里 
"""

#----- content starts here -----
"""
Suppose there are a good horse and a slow horse departing from Chang'an to Qi. The distance from Qi to Chang'an is 3000 li.
The good horse travels 193 li on the first day and increases its daily travel by 13 li each day.
The slow horse travels 97 li on the first day and decreases its daily travel by 0.5 li each day.
The good horse arrives at Qi first, then returns to meet the slow horse.
Question: How many days until they meet, and how far does each horse travel?

The procedure says: Suppose for 15 days, the distance is insufficient by 337.5 li.
Suppose for 16 days, the distance exceeds by 140 li.
Multiply the excess and deficiency by the supposed number of days, add them together to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to obtain the number of days.
If there is a remainder, divide it by the equal number to determine the fraction.

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

# 假令十五日不足三百三十七里半
假令_15日 = 15
不足 = 337.5

# 假令十六日多一百四十里
假令_16日 = 16
多 = 140

# 以盈不足維乘假令之數并而為實
實 = (不足 * 假令_16日) + (多 * 假令_15日)

# 并盈不足為法
法 = 不足 + 多

# 實如法而一得日數
日數 = Fraction(實, 法)

# 計算良馬與駑馬的行程
良馬行程 = sum([良馬初日 + i * 良馬日增 for i in range(int(日數))])
駑馬行程 = sum([駑馬初日 - i * 駑馬日減 for i in range(int(日數))])

a = 日數
b = 良馬行程
c = 駑馬行程#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
