"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

#----- content starts here -----
"""
Suppose there is a supply of millet for five people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi. 
In total, they have 15 dou of millet. 
Now, an additional Daifu arrives, who is also supposed to receive 5 dou. 
However, there is no more millet in the granary, so the millet must be redistributed according to their ranks. 
Question: how much does each person contribute?

The procedure says: 
List the millet amounts each person originally receives in dou. 
Adjust these amounts according to their ranks, forming a sequence of decreasing weights. 
Add the weights together, including the additional 5 dou for the new Daifu, to form the divisor. 
Multiply the 5 dou by the weights of the original recipients to form the dividend for each. 
Divide the dividend by the divisor to determine how much each person contributes.

Answer: the Daifu contributes *a* dou, the Bugeng contributes *b* dou, the Zanniao contributes *c* dou, the Shangzao contributes *d* dou, and the Gongshi contributes *e* dou.
"""

from fractions import Fraction

# Initial millet distribution (in dou)
initial_distribution = [5, 4, 3, 2, 1]  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi

# Additional Daifu's share
additional_daifu_share = 5

# Calculate the divisor (法)
法 = sum(initial_distribution) + additional_daifu_share

# Calculate the dividend (實) for each person
實 = [5 * weight for weight in initial_distribution]

# Calculate the contribution of each person
a, b, c, d, e = [Fraction(value, 法) for value in 實]

# Output the results
a, b, c, d, e  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi contributions#----- content ends here -----

"""
"""
