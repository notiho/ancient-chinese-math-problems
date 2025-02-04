"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

"""
Suppose there is a total of 15 dou of millet distributed among five people: a Daifu, a Bugeng, a Zanniao, a Shangzao, and a Gongshi, according to their ranks. 
Now, another Daifu arrives and is also entitled to 5 dou of millet. However, the granary is empty, so the millet must be redistributed proportionally based on their ranks.

Question: how much millet does each person contribute to the new Daifu?

Answer: the Daifu contributes *a* dou, the Bugeng contributes *b* dou, the Zanniao contributes *c* dou, the Shangzao contributes *d* dou, and the Gongshi contributes *e* dou.
"""

# Original shares based on rank
original_shares = [5, 4, 3, 2, 1]  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi

# Total millet to be redistributed
total_millet_needed = 5  # The new Daifu needs 5 dou

# Total rank sum
total_rank_sum = sum(original_shares)

# Calculate how much each person contributes proportionally
a, b, c, d, e = [Fraction(total_millet_needed * share, total_rank_sum) for share in original_shares]

# Results
a, b, c, d, e  # These are the contributions in dou from each person.
"""
Variable 'a' has wrong value. Expected: 5/4, Actual: 5/3
Variable 'b' has wrong value. Expected: 1, Actual: 4/3
Variable 'c' has wrong value. Expected: 3/4, Actual: 1
Variable 'd' has wrong value. Expected: 1/2, Actual: 2/3
Variable 'e' has wrong value. Expected: 1/4, Actual: 1/3"""
