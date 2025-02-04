"""
今有駑馬日初發家良馬日以七分之一發家日乃五分之二行四十五里及駑馬問良駑馬一日不止各行㡬何
術曰置五分之二七分之一相減餘為良馬行率増七分日之一為駑馬行率各以為法以及里數乗二母為實實如法而一
答曰良馬日行 a里 駑馬日行 b里
"""

#----- content starts here -----
"""
Suppose there is a slow horse (nu ma) and a good horse (liang ma). 
The slow horse starts traveling at dawn, while the good horse starts traveling later, after 1/7 of the day has passed.
By the end of the day, the good horse has traveled 2/5 of the distance that the slow horse has traveled in 45 li.
Question: how far does each horse travel in one day without stopping?

The procedure says: Subtract 2/5 from 1/7, and the remainder is the rate of travel for the good horse.
Add 1/7 to the rate of travel for the slow horse.
Take these as the divisors (fa).
Multiply the total distance (45 li) by twice the denominators to obtain the dividends (shi).
Divide the dividends by the divisors to obtain the distances traveled by each horse in one day.

Answer: The good horse travels *a* li in one day, and the slow horse travels *b* li in one day.
"""

from fractions import Fraction

# 良馬日以七分之一發家
良馬延遲 = Fraction(1, 7)

# 日乃五分之二行
良馬比例 = Fraction(2, 5)

# 駑馬日初發家
駑馬比例 = 1  # 駑馬比例 is the full day rate (1 full day).

# 置五分之二七分之一相減，餘為良馬行率
良馬行率 = 駑馬比例 - 良馬比例

# 増七分之一為駑馬行率
駑馬行率 = 駑馬比例 + 良馬延遲

# 以及里數 (45里)
里數 = 45

# 各以為法
良馬法 = 良馬行率
駑馬法 = 駑馬行率

# 乘二母為實
良馬實 = 2 * 里數 * 駑馬法.denominator * 良馬法.denominator
駑馬實 = 2 * 里數 * 駑馬法.denominator * 良馬法.denominator

# 實如法而一
a = Fraction(良馬實, 良馬法 * 2 * 駑馬法.denominator)
b = Fraction(駑馬實, 駑馬法 * 2 * 良馬法.denominator)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 175, Actual: 375
Variable 'b' has wrong value. Expected: 225/2, Actual: 2205/8"""
