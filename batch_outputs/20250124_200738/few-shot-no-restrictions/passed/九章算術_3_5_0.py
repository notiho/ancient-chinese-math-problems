"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

#----- content starts here -----
"""
Suppose there is a supply of millet for five people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi. 
In total, they have 15 dou of millet. 
Now, an additional Daifu arrives and is also supposed to receive 5 dou. 
However, there is no more millet in the granary, so the millet must be redistributed proportionally according to their ranks.
Question: how much does each contribute?

The procedure says: Place the millet amounts each person is supposed to receive (in hu and dou) and adjust them according to their ranks, forming a proportional sequence. 
Add the additional 5 dou for the arriving Daifu, making the total 20 dou, which becomes the divisor.
Multiply the 5 dou by the proportional sequence (excluding the sum), forming the dividend for each person.
Divide the dividend by the divisor to determine how much each person contributes.

Answer: the Daifu contributes *a* dou, the Bugeng contributes *b* dou, the Zanniao contributes *c* dou, the Shangzao contributes *d* dou, and the Gongshi contributes *e* dou.
"""

from fractions import Fraction

# Initial millet distribution (in dou)
initial_millet = 15

# Additional Daifu arrives, requiring 5 dou
additional_millet = 5

# Total millet to redistribute
total_millet = initial_millet + additional_millet

# Ranks and their corresponding millet amounts
ranks = [5, 4, 3, 2, 1]  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi
additional_daifu_millet = 5

# Add the additional Daifu's millet to the total divisor
法 = sum(ranks) + additional_daifu_millet

# Calculate each person's contribution
實 = [5 * rank for rank in ranks]  # Multiply 5 dou by each rank
contributions = [Fraction(value, 法) for value in 實]

# Assign contributions to each rank
a, b, c, d, e = contributions

# Output the results
a, b, c, d, e  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi contributions#----- content ends here -----

"""
"""
