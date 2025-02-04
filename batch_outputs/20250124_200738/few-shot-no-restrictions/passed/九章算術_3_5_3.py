"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

#----- content starts here -----
"""
Suppose there is millet to be distributed among five people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi. 
In total, they have 15 dou of millet. 
Now, an additional Daifu arrives and is also entitled to 5 dou. 
However, there is no more millet in the granary, so the millet must be redistributed proportionally according to their ranks.
Question: how much does each person contribute?

The procedure says: Place the millet amounts (in hu and dou) that each person originally received, and divide them according to their ranks, forming a sequence of proportional contributions.
Add the 5 dou for the newly arrived Daifu to the total, making 20 dou in total as the divisor.
Multiply 5 dou by the proportional contributions of each person to form the dividend.
Divide the dividend by the divisor to find the amount each person contributes.

Answer: the Daifu contributes *a* dou, the Bugeng contributes *b* dou, the Zanniao contributes *c* dou, the Shangzao contributes *d* dou, and the Gongshi contributes *e* dou.
"""

from fractions import Fraction

# Original millet distribution (in dou)
original_distribution = [5, 4, 3, 2, 1]  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi

# Add the 5 dou for the new Daifu
new_daifu = 5
total_millet = sum(original_distribution) + new_daifu  # Total millet = 15 + 5 = 20

# Calculate the proportional contributions (列衰)
法 = total_millet  # The divisor is the total millet = 20
proportional_contributions = [5 * i for i in original_distribution]  # Multiply each by 5 (未并者)

# Calculate the amount each person contributes
a, b, c, d, e = [Fraction(i, 法) for i in proportional_contributions]

# Output results
a, b, c, d, e  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi contributions#----- content ends here -----

"""
"""
