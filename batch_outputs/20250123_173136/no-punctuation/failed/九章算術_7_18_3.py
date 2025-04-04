"""
今有良馬與駑馬發長安至齊齊去長安三千里良馬初日行一百九十三里日增十三里駑馬初日行九十七里日減半里良馬先至齊復還迎駑馬問幾何日相逢及各行幾何
術曰假令十五日不足三百三十七里半令之十六日多一百四十里以盈不足維乘假令之數并而為實并盈不足為法實如法而一得日數不盡者以等數除之而命分
荅曰 a日 而相逢良馬行 b里 駑馬行 c里 
"""

"""
Suppose there are a fine horse and a slow horse departing from Chang'an to Qi. Qi is 3000 li away from Chang'an.
The fine horse travels 193 li on the first day, increasing its daily distance by 13 li each day.
The slow horse travels 97 li on the first day, decreasing its daily distance by 0.5 li each day.
The fine horse reaches Qi first, then returns to meet the slow horse.
Question: how many days until they meet, and how far has each traveled?

The procedure says: Suppose 15 days, which is insufficient by 337.5 li.
Suppose 16 days, which is excessive by 140 li.
Multiply the excess and deficiency by the supposed number of days, add them together to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to obtain the number of days.
If there is a remainder, divide it by the difference in daily travel rates to determine the fraction.

Answer: *a* days until they meet, the fine horse travels *b* li, and the slow horse travels *c* li.
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

# 計算良馬行距離
良馬行距離 = 0
for i in range(1, int(日數) + 1):
    良馬行距離 += 良馬初日 + (i - 1) * 良馬日增

# 計算駑馬行距離
駑馬行距離 = 0
for i in range(1, int(日數) + 1):
    駑馬行距離 += 駑馬初日 - (i - 1) * 駑馬日減

# 如果有餘數，計算剩餘部分
餘數 = 日數 - int(日數)
if 餘數 > 0:
    良馬行距離 += 餘數 * (良馬初日 + int(日數) * 良馬日增)
    駑馬行距離 += 餘數 * (駑馬初日 - int(日數) * 駑馬日減)

a = 日數
b = 良馬行距離
c = 駑馬行距離
"""
Code error: both arguments should be Rational instances"""
