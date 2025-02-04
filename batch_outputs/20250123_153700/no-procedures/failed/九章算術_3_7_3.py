"""
今有大夫、不更、簪褭、上造、公士，凡五人，共出百錢。欲令高爵出少，以次漸多，問︰各幾何？
荅曰：大夫出 a錢 。不更出 b錢 。簪褭出 c錢 。上造出 d錢 。公士出 e錢 。
"""

"""
Suppose there are five people: Daifu, Bugeng, Zanniao, Shangzao, and Gongshi. Together, they contribute 100 qian.
It is desired that the higher the rank, the less they contribute, and the contributions increase gradually by rank.

Question: How much does each contribute?

Answer: The Daifu contributes *a* qian, the Bugeng contributes *b* qian, the Zanniao contributes *c* qian, the Shangzao contributes *d* qian, and the Gongshi contributes *e* qian.
"""

# The contributions are inversely proportional to their ranks.
# Assign weights to the contributions based on rank: Daifu = 1, Bugeng = 2, Zanniao = 3, Shangzao = 4, Gongshi = 5.
weights = [1, 2, 3, 4, 5]

# Total contribution
total_contribution = 100

# Calculate the total weight
total_weight = sum(weights)

# Calculate each person's contribution
a, b, c, d, e = [Fraction(weight * total_contribution, total_weight) for weight in weights]

# Output the results
a, b, c, d, e
"""
Variable 'a' has wrong value. Expected: 1200/137, Actual: 20/3
Variable 'b' has wrong value. Expected: 1500/137, Actual: 40/3
Variable 'c' has wrong value. Expected: 2000/137, Actual: 20
Variable 'd' has wrong value. Expected: 3000/137, Actual: 80/3
Variable 'e' has wrong value. Expected: 6000/137, Actual: 100/3"""
