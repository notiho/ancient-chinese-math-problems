"""
今有駑馬日初發家良馬日以七分之一發家日乃五分之二行四十五里及駑馬問良駑馬一日不止各行㡬何
術曰置五分之二七分之一相減餘為良馬行率増七分日之一為駑馬行率各以為法以及里數乗二母為實實如法而一
答曰良馬日行 a里 駑馬日行 b里
"""

"""
Suppose there is a slow horse (駑馬) and a good horse (良馬). 
The slow horse departs from home at the start of the day, while the good horse departs later, after 1/7 of the day has passed.
By the end of the day, the good horse has traveled 2/5 of the distance traveled by the slow horse, and the total distance traveled by both is 45 li.
Question: how far does each horse travel in one day without stopping?

The procedure says: Subtract 1/7 from 2/5, and the remainder is the rate of travel for the good horse.
Add 1/7 to the rate of travel for the slow horse.
Use these as the divisors (法).
Multiply the total distance (45 li) by twice the denominators (母) of the fractions to obtain the dividends (實).
Divide the dividends by the divisors to find the distances traveled by each horse.

Answer: the good horse travels *a* li per day, and the slow horse travels *b* li per day.
"""

from fractions import Fraction

# 良馬日以五分之二
良馬率 = Fraction(2, 5)

# 駑馬日以七分之一
駑馬率 = Fraction(1, 7)

# 置五分之二七分之一相減，餘為良馬行率
良馬行率 = 良馬率 - 駑馬率

# 増七分之一為駑馬行率
駑馬行率 = 良馬行率 + 駑馬率

# 以及里數
總里數 = 45

# 乘二母為實
實 = 總里數 * 2 * (良馬行率.denominator * 駑馬行率.denominator)

# 實如法而一
a = Fraction(實, 良馬行率.denominator * 2)
b = Fraction(實, 駑馬行率.denominator * 2)
"""
Variable 'a' has wrong value. Expected: 175, Actual: 225
Variable 'b' has wrong value. Expected: 225/2, Actual: 1575"""
