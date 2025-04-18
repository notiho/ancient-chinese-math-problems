"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

"""

"""


from fractions import Fraction

# 各置所稟粟斛斗數，爵次均之，以為列衰
爵次 = [5, 4, 3, 2, 1]  # 大夫、不更、簪裹、上造、公士
後來大夫稟粟 = 5  # 後來大夫稟粟五斗

# 副并而加後來大夫亦五斗，得二十以為法
法 = sum(爵次) + 後來大夫稟粟

# 以五斗乘未并者各自為實
實 = [5 * i for i in 爵次]

# 實如法得一斗
a, b, c, d, e = [Fraction(i, 法) for i in 實]

# Output results
a, b, c, d, e


"""
 

This code calculates the amount of 粟 (grain) each person contributes based on their rank and the given procedure. The results are fractions representing the contribution of each rank.
"""


"""
"""
