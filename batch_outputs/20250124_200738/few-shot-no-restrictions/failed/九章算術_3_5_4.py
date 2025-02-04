"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
術曰：各置所稟粟斛斗數，爵次均之，以為列衰，副并而加後來大夫亦五斗，得二十以為法。以五斗乘未并者各自為實。實如法得一斗。
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

#----- content starts here -----
"""
Suppose there is millet stored in a granary. There are five people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi. 
Together, they are to receive 15 dou of millet. 
Now, an additional Daifu arrives later, and they are also to receive 5 dou. 
However, the granary has no more millet, so the millet must be redistributed proportionally based on rank. 
Question: how much does each person contribute?

The procedure says: Place the millet amounts (in hu and dou) that each person is to receive, and balance them according to rank. 
This forms the proportional sequence. 
Add the auxiliary amounts and include the 5 dou for the newly arrived Daifu, obtaining 20 as the divisor. 
Multiply the 5 dou by the unbalanced amounts, forming the dividend for each. 
Divide the dividend by the divisor to obtain the amount each person contributes.

Answer: the Daifu contributes *a* dou, the Bugeng contributes *b* dou, the Zanniao contributes *c* dou, the Shangzao contributes *d* dou, and the Gongshi contributes *e* dou.
"""

from fractions import Fraction

# Initial millet distribution (in dou)
initial_distribution = {
    "Daifu": 5,
    "Bugeng": 4,
    "Zanniao": 3,
    "Shangzao": 2,
    "Gongshi": 1,
}

# Total millet to redistribute, including the additional Daifu's 5 dou
total_millet = 15 + 5  # 20 dou

# Proportional sequence based on rank
proportions = [5, 4, 3, 2, 1]  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi

# Calculate the divisor (法)
法 = sum(proportions)

# Calculate the dividend (實) for each person
實 = [5 * p for p in proportions]

# Divide each 实 by 法 to get the contribution of each person
a, b, c, d, e = [Fraction(s, 法) for s in 實]

# Output the results
print(f"Daifu contributes {a} dou.")
print(f"Bugeng contributes {b} dou.")
print(f"Zanniao contributes {c} dou.")
print(f"Shangzao contributes {d} dou.")
print(f"Gongshi contributes {e} dou.")#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/4, Actual: 5/3
Variable 'b' has wrong value. Expected: 1, Actual: 4/3
Variable 'c' has wrong value. Expected: 3/4, Actual: 1
Variable 'd' has wrong value. Expected: 1/2, Actual: 2/3
Variable 'e' has wrong value. Expected: 1/4, Actual: 1/3"""
