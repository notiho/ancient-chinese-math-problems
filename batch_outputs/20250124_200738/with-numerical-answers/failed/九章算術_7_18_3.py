"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
術曰：假令十五日，不足三百三十七里半。令之十六日，多一百四十里。以盈、不足維乘假令之數，并而為實。并盈不足為法。實如法而一，得日數。不盡者，以等數除之而命分。
荅曰： a(=3000/191)日 而相逢。良馬行 b(=866040/191)里 。駑馬行 c(=279960/191)里 。
"""

#----- content starts here -----
"""
Suppose there are a fine horse and a slow horse traveling from Chang'an to Qi. The distance from Qi to Chang'an is 3000 li.
The fine horse travels 193 li on the first day and increases its daily travel by 13 li each day.
The slow horse travels 97 li on the first day and decreases its daily travel by 0.5 li each day.
The fine horse reaches Qi first, then returns to meet the slow horse.
Question: after how many days do they meet, and how far does each travel?

The procedure says: Suppose it takes 15 days, and the distance is short by 337.5 li. Suppose it takes 16 days, and the distance exceeds by 140 li.
Multiply the excess and shortfall by the respective assumed days, then add them to form the dividend.
Add the excess and shortfall to form the divisor.
Divide the dividend by the divisor to obtain the number of days. If there is a remainder, divide it by the difference in daily rates to determine the fraction.

Answer: *a*(=3000/191) days until they meet. The fine horse travels *b*(=866040/191) li, and the slow horse travels *c*(=279960/191) li.
"""

from fractions import Fraction

# 齊去長安三千里
總距離 = 3000

# 良馬初日行一百九十三里，日增十三里
良馬初日 = 193
良馬日增 = 13

# 駑馬初日行九十七里，日減半里
駑馬初日 = 97
駑馬日減 = Fraction(1, 2)

# 假令十五日，不足三百三十七里半
假令1 = 15
不足 = 337.5

# 令之十六日，多一百四十里
假令2 = 16
多 = 140

# 以盈、不足維乘假令之數，并而為實
實 = (多 * 假令1) + (不足 * 假令2)

# 并盈不足為法
法 = 多 + 不足

# 實如法而一，得日數
日數 = Fraction(實, 法)

# 計算良馬與駑馬的行程
良馬行程 = sum(良馬初日 + i * 良馬日增 for i in range(int(日數)))
駑馬行程 = sum(駑馬初日 - i * 駑馬日減 for i in range(int(日數)))

# 良馬行程與駑馬行程的分數表示
a = 日數  # 3000/191
b = Fraction(總距離 * 3, a#----- content ends here -----

"""
Code error: '(' was never closed (<string>, line 53)"""
