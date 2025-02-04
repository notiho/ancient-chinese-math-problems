"""
今有大夫、不更、簪褭、上造、公士，凡五人，共出百錢。欲令高爵出少，以次漸多，問︰各幾何？
荅曰：大夫出 a錢 。不更出 b錢 。簪褭出 c錢 。上造出 d錢 。公士出 e錢 。
"""

#----- content starts here -----
"""
Suppose there are five individuals: Daifu, Bugeng, Zanniao, Shangzao, and Gongshi (official titles of varying ranks). 
Together, they contribute 100 qian (coins). It is desired that the higher-ranking individuals contribute less, and the lower-ranking individuals contribute more, in a gradually increasing manner.
Question: how much does each contribute?

Answer: Daifu contributes *a* qian, Bugeng contributes *b* qian, Zanniao contributes *c* qian, Shangzao contributes *d* qian, and Gongshi contributes *e* qian.
"""

# The contributions are proportional to their ranks, with higher ranks contributing less.
# Assign weights to each rank (higher rank = smaller weight).
weights = [1, 2, 3, 4, 5]  # Daifu to Gongshi

# Total contribution
total_contribution = 100

# Calculate the total weight
total_weight = sum(weights)

# Calculate each individual's contribution
a, b, c, d, e = [Fraction(weight * total_contribution, total_weight) for weight in weights]

# Output the results
a, b, c, d, e  # Daifu, Bugeng, Zanniao, Shangzao, Gongshi contributions#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 1200/137, Actual: 20/3
Variable 'b' has wrong value. Expected: 1500/137, Actual: 40/3
Variable 'c' has wrong value. Expected: 2000/137, Actual: 20
Variable 'd' has wrong value. Expected: 3000/137, Actual: 80/3
Variable 'e' has wrong value. Expected: 6000/137, Actual: 100/3"""
