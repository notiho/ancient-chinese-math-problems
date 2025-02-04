"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

#----- content starts here -----
"""
Suppose there is a distribution of millet. There are five people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi. 
In total, they have 15 dou of millet. Now, one more Daifu arrives later, and he should also receive 5 dou. 
However, the granary is empty, so the millet must be redistributed proportionally according to their ranks. 
Question: how much does each person contribute?

The procedure says: Place the millet amounts each person originally received (in hu and dou) and balance them according to their ranks, forming a proportional sequence. 
Add the 5 dou for the newly arrived Daifu to the total, making 20 dou the divisor. 
Multiply the 5 dou by the proportional sequence for each person, forming the dividend. 
Divide the dividend by the divisor to find the amount each person contributes.

Answer: The Daifu contributes *a* dou, the Bugeng contributes *b* dou, the Zanniao contributes *c* dou, the Shangzao contributes *d* dou, and the Gongshi contributes *e* dou.
"""

from fractions import Fraction

# Original millet distribution (in dou)
original_distribution = [5, 4, 3, 2, 1]  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi

# Add the newly arrived Daifu's 5 dou
new_daifu_millet = 5
total_millet = sum(original_distribution) + new_daifu_millet  # 15 + 5 = 20

# Total divisor (法)
法 = total_millet

# Calculate the contribution of each person
# Multiply the new Daifu's 5 dou by the original distribution
實 = [new_daifu_millet * rank for rank in original_distribution]

# Divide each by the total divisor
a, b, c, d, e = [Fraction(contribution, 法) for contribution in 實]

# Output the results
a, b, c, d, e  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi contributions#----- content ends here -----

"""
"""
