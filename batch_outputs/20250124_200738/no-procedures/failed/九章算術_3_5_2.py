"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

#----- content starts here -----
"""
Suppose there are 5 people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi. Together, they have 15 dou of millet. 
Now, another Daifu arrives and also needs to receive 5 dou. However, there is no more millet in the granary, so the original 5 people must contribute millet proportionally to their ranks.

Question: how much does each person contribute?

Answer: the Daifu contributes *a* dou, the Bugeng contributes *b* dou, the Zanniao contributes *c* dou, the Shangzao contributes *d* dou, and the Gongshi contributes *e* dou.
"""

# Total millet to be contributed
total_contribution = 5  # The new Daifu needs 5 dou

# Original shares based on rank
shares = [5, 4, 3, 2, 1]  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi

# Total weight of shares
total_shares = sum(shares)

# Calculate the contribution of each person proportionally
a, b, c, d, e = [Fraction(total_contribution * share, total_shares) for share in shares]

# Results
a, b, c, d, e  # These are the contributions of Daifu, Bugeng, Zanniao, Shangzao, and Gongshi respectively.#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5/4, Actual: 5/3
Variable 'b' has wrong value. Expected: 1, Actual: 4/3
Variable 'c' has wrong value. Expected: 3/4, Actual: 1
Variable 'd' has wrong value. Expected: 1/2, Actual: 2/3
Variable 'e' has wrong value. Expected: 1/4, Actual: 1/3"""
