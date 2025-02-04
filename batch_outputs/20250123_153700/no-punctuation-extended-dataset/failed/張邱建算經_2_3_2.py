"""
今有駑馬日初發家良馬日以七分之一發家日乃五分之二行四十五里及駑馬問良駑馬一日不止各行㡬何
術曰置五分之二七分之一相減餘為良馬行率増七分日之一為駑馬行率各以為法以及里數乗二母為實實如法而一
答曰良馬日行 a里 駑馬日行 b里
"""

"""
Suppose there is a slow horse (駑馬) and a good horse (良馬). 
The slow horse starts traveling at dawn, while the good horse starts traveling after 1/7 of the day has passed. 
By the time the good horse has traveled 2/5 of the day, they have both traveled 45 li.
Question: how far does each horse travel in one full day without stopping?

The procedure says: Subtract 2/5 and 1/7, the remainder is the rate of the good horse's travel.
Add 1/7 of the day to the slow horse's rate, this is the rate of the slow horse's travel.
Take each rate as the divisor. Multiply the distance (45 li) by 2 times the denominators of the rates, this is the dividend.
Divide the dividend by the divisor to obtain the distance traveled in one day.

Answer: the good horse travels *a* li per day, and the slow horse travels *b* li per day.
"""

from fractions import Fraction

# 良馬日以七分之一發家
良馬延遲 = Fraction(1, 7)

# 良馬日乃五分之二行
良馬行時間 = Fraction(2, 5)

# 行四十五里
距離 = 45

# 置五分之二七分之一相減，餘為良馬行率
良馬行率 = 良馬行時間 - 良馬延遲

# 増七分之一為駑馬行率
駑馬行率 = Fraction(1, 1) - 良馬延遞

# 各以為法
良馬法 = 良馬行率
駑馬法 = 駑馬行率

# 以及里數乘二母為實
實 = 距離 * 2 * (良馬法.denominator * 駑馬法.denominator)

# 實如法而一
a = Fraction(實, 良馬法)
b = Fraction(實, 駑馬法)
"""
Code error: name '良馬延遞' is not defined"""
