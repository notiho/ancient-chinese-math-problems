"""
今有大夫、不更、簪褭、上造、公士，凡五人，共出百錢。欲令高爵出少，以次漸多，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：置爵數各自為衰，而返衰之，副并為法。以百錢乘未并者各自為實。實如法得一錢。
荅曰：大夫出 a錢 。不更出 b錢 。簪褭出 c錢 。上造出 d錢 。公士出 e錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing 100 coins among five people with decreasing contributions based on their ranks. The solution involves using the method described in the text.

Here is the Python code:


"""


from fractions import Fraction

# Define the ranks and their respective weights (衰)
# Higher rank contributes less, so weights are inversely proportional
weights = [1, 2, 3, 4, 5]  # 大夫, 不更, 簪褭, 上造, 公士

# Calculate the total weight (sum of weights)
total_weight = sum(weights)

# Calculate the contributions based on the weights
a = Fraction(100, total_weight) * weights[0]  # 大夫
b = Fraction(100, total_weight) * weights[1]  # 不更
c = Fraction(100, total_weight) * weights[2]  # 簪褭
d = Fraction(100, total_weight) * weights[3]  # 上造
e = Fraction(100, total_weight) * weights[4]  # 公士

# Output the results
a, b, c, d, e


"""


### Explanation:
1. **Weights**: The weights are assigned as `[1, 2, 3, 4, 5]` corresponding to the ranks from highest to lowest (大夫, 不更, 簪褭, 上造, 公士).
2. **Total Weight**: The sum of the weights is calculated as `1 + 2 + 3 + 4 + 5 = 15`.
3. **Contributions**: Each person's contribution is proportional to their weight, calculated as `(100 / total_weight) * weight`.

### Results:
The contributions are:
- 大夫 (a): \( \frac{100}{15} \times 1 = \frac{20}{3} \) coins
- 不更 (b): \( \frac{100}{15} \times 2 = \frac{40}{3} \) coins
- 簪褭 (c): \( \frac{100}{15} \times 3 = 20 \) coins
- 上造 (d): \( \frac{100}{15} \times 4 = \frac{80}{3} \) coins
- 公士 (e): \( \frac{100}{15} \times 5 = \frac{100}{3} \) coins
"""


"""
Variable 'a' has wrong value. Expected: 1200/137, Actual: 20/3
Variable 'b' has wrong value. Expected: 1500/137, Actual: 40/3
Variable 'c' has wrong value. Expected: 2000/137, Actual: 20
Variable 'd' has wrong value. Expected: 3000/137, Actual: 80/3
Variable 'e' has wrong value. Expected: 6000/137, Actual: 100/3"""
