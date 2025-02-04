"""
今有駑馬日初發家良馬日以七分之一發家日乃五分之二行四十五里及駑馬問良駑馬一日不止各行㡬何
術曰置五分之二七分之一相減餘為良馬行率増七分日之一為駑馬行率各以為法以及里數乗二母為實實如法而一
答曰良馬日行 a里 駑馬日行 b里
"""

"""
Suppose there is a slow horse (駑馬) and a good horse (良馬). 
The slow horse departs from home at the start of the day, while the good horse departs later in the day, after 1/7 of the day has passed. 
By the end of the day, the good horse has traveled 2/5 of the distance that the slow horse traveled, and together they have covered 45 li. 
Question: how far does each horse travel in one day without stopping?

The procedure says: Subtract 2/5 from 1/7, and the remainder is the rate at which the good horse travels.
Add 1/7 to the rate of the slow horse, and this becomes the rate at which the slow horse travels.
Take each rate as the divisor, and multiply the total distance (45 li) by the product of the two denominators to obtain the dividend.
Divide the dividend by the divisor to obtain the distance traveled by each horse.

Answer: the good horse travels *a* li per day, and the slow horse travels *b* li per day.
"""

from fractions import Fraction

# 良馬日以七分之一發家
良馬延遲 = Fraction(1, 7)

# 日乃五分之二行
良馬行率 = Fraction(2, 5)

# 駑馬行率 (日初發家)
駑馬行率 = 1 - 良馬延遲

# 置五分之二七分之一相減，餘為良馬行率
良馬實際行率 = 良馬行率 - 良馬延遲

# 増七分之一為駑馬行率
駑馬實際行率 = 駑馬行率 + 良馬延遲

# 各以為法
良馬法 = 良馬實際行率
駑馬法 = 駑馬實際行率

# 以及里數乘二母為實
總里數 = 45
實 = 總里數 * (良馬法.denominator * 駑馬法.denominator)

# 實如法而一
a = Fraction(實, 良馬法.denominator * 駑馬法.numerator)
b = Fraction(實, 駑馬法.denominator * 良馬法.numerator)
"""
Variable 'a' has wrong value. Expected: 175, Actual: 45
Variable 'b' has wrong value. Expected: 225/2, Actual: 175"""
