"""
今有稟粟，大夫、不更、簪裹、上造、公士，凡五人，一十五斗。今有大夫一人後來，亦當稟五斗。倉無粟，欲以衰出之，問︰各幾何？
荅曰：大夫出 a斗 。不更出 b斗 。簪褭出 c斗 。上造出 d斗 。公士出 e斗 。
"""

"""
Suppose there is a stock of millet, distributed among five people: Daifu, Bugeng, Zanniao, Shangzao, and Gongshi. 
In total, they have 15 dou of millet. Now, another Daifu arrives and also needs to receive 5 dou. 
Since there is no more millet in the storehouse, the millet must be redistributed proportionally according to their ranks.

Question: how much millet does each person contribute?

Answer: Daifu contributes *a* dou, Bugeng contributes *b* dou, Zanniao contributes *c* dou, Shangzao contributes *d* dou, and Gongshi contributes *e* dou.
"""

# Initial millet distribution
total_millet = 15  # in dou
new_daifu_millet = 5  # in dou

# Shares based on rank
shares = [5, 4, 3, 2, 1]  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi

# Total shares
total_shares = sum(shares)

# Millet each rank initially holds
initial_distribution = [Fraction(total_millet * share, total_shares) for share in shares]

# Total millet needed to redistribute
millet_to_redistribute = new_daifu_millet

# Redistribute proportionally based on shares
redistribution = [Fraction(millet_to_redistribute * share, total_shares) for share in shares]

# Calculate how much each person contributes
a, b, c, d, e = redistribution

# Output results
a, b, c, d, e  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi contributions
"""
Variable 'a' has wrong value. Expected: 5/4, Actual: 5/3
Variable 'b' has wrong value. Expected: 1, Actual: 4/3
Variable 'c' has wrong value. Expected: 3/4, Actual: 1
Variable 'd' has wrong value. Expected: 1/2, Actual: 2/3
Variable 'e' has wrong value. Expected: 1/4, Actual: 1/3"""
