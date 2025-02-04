"""
今有駑馬日初發家良馬日以七分之一發家日乃五分之二行四十五里及駑馬問良駑馬一日不止各行㡬何
術曰置五分之二七分之一相減餘為良馬行率増七分日之一為駑馬行率各以為法以及里數乗二母為實實如法而一
答曰良馬日行 a里 駑馬日行 b里
"""

#----- content starts here -----
"""
Suppose there is a slow horse (駑馬) and a good horse (良馬). 
The slow horse starts traveling from home at dawn, while the good horse starts traveling later in the day, after 1/7 of the day has passed. 
By the time the good horse has traveled 2/5 of a day, they have both covered 45 li.
Question: how far does each horse travel in one full day without stopping?

The procedure says: Subtract 2/5 from 1/7, and the remainder is the rate of the good horse's travel.
Add 1/7 to the rate of the slow horse's travel, and this is the rate of the slow horse's travel.
Take these rates as divisors.
Multiply the distance (45 li) by the denominators of both fractions to obtain the dividends.
Divide the dividends by their respective divisors to obtain the daily distances traveled by each horse.

Answer: the good horse travels *a* li per day, and the slow horse travels *b* li per day.
"""

from fractions import Fraction

# 良馬日以七分之一發家
良馬延遲 = Fraction(1, 7)

# 日乃五分之二行
良馬行時間 = Fraction(2, 5)

# 行四十五里
距離 = 45

# 置五分之二七分之一相減，餘為良馬行率
良馬行率 = Fraction(1, 良馬延遲) - Fraction(1, 良馬行時間)

# 増七分日之一為駑馬行率
駑馬行率 = Fraction(1, 良馬延遲 )#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
