"""
今有良馬與駑馬發長安至齊。齊去長安三千里。良馬初日行一百九十三里，日增十三里。駑馬初日行九十七里，日減半里。良馬先至齊，復還迎駑馬。問︰幾何日相逢及各行幾何？
術曰：假令十五日，不足三百三十七里半。令之十六日，多一百四十里。以盈、不足維乘假令之數，并而為實。并盈不足為法。實如法而一，得日數。不盡者，以等數除之而命分。
荅曰： a(=3000/191)日 而相逢。良馬行 b(=866040/191)里 。駑馬行 c(=279960/191)里 。
"""

#----- content starts here -----
"""
Suppose there are a fine horse and a slow horse departing from Chang'an to Qi. The distance from Qi to Chang'an is 3000 li.
The fine horse travels 193 li on the first day, increasing its daily distance by 13 li each day.
The slow horse travels 97 li on the first day, decreasing its daily distance by 0.5 li each day.
The fine horse reaches Qi first, then returns to meet the slow horse.
Question: after how many days do they meet, and how far does each travel?

The procedure says: Suppose it takes 15 days, it is short by 337.5 li. Suppose it takes 16 days, it exceeds by 140 li.
Multiply the surplus and deficit by their respective assumed days, then add them to form the dividend.
Add the surplus and deficit to form the divisor.
Divide the dividend by the divisor to get the number of days.
If there is a remainder, divide it by the difference to determine the fraction.

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
不足 = Fraction(337.5)
假令_不足 = 15

# 令之十六日，多一百四十里
盈 = 140
假令_盈 = 16

# 以盈、不足維乘假令之數，并而為實
實 = (盈 * 假令_不足) + (不足 * 假令_盈)

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一，得日數
日數 = Fraction(實, 法)

# 良馬行的總距離
良馬行距離 = sum(良馬初日 + i * 良馬日增 for i in range(int(日數)))

# 駑馬行的總距離
駑馬行距離 = sum(駑馬初日 - i * 駑馬日減 for i in range(int(日數)))

# 良馬和駑馬相遇
a = 日數
b = Fraction(總距離 * 2 )#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 866040/191, Actual: 6000
Missing variable in output: 'c'"""
