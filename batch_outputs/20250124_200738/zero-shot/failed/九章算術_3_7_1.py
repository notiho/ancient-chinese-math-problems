"""
今有大夫、不更、簪褭、上造、公士，凡五人，共出百錢。欲令高爵出少，以次漸多，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：置爵數各自為衰，而返衰之，副并為法。以百錢乘未并者各自為實。實如法得一錢。
荅曰：大夫出 a錢 。不更出 b錢 。簪褭出 c錢 。上造出 d錢 。公士出 e錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves distributing 100 coins among five ranks (大夫, 不更, 簪褭, 上造, 公士) such that the higher the rank, the fewer coins they contribute, and the lower the rank, the more coins they contribute. The solution involves using the "返衰術" (reversal of proportionality) method.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the ranks' proportional weights (衰)
# Higher ranks have smaller weights, and lower ranks have larger weights
weights = [1, 2, 3, 4, 5]  # 大夫, 不更, 簪褭, 上造, 公士

# Reverse the weights (返衰之)
reversed_weights = [Fraction(1, w) for w in weights]

# Sum of reversed weights (副并为法)
total_reversed_weight = sum(reversed_weights)

# Calculate the amount of money each rank contributes
# (以百錢乘未并者各自为实，实如法得一錢)
total_money = 100
a = Fraction(total_money) * reversed_weights[0] / total_reversed_weight  # 大夫
b = Fraction(total_money) * reversed_weights[1] / total_reversed_weight  # 不更
c = Fraction(total_money) * reversed_weights[2] / total_reversed_weight  # 簪褭
d = Fraction(total_money) * reversed_weights[3] / total_reversed_weight  # 上造
e = Fraction(total_money) * reversed_weights[4] / total_reversed_weight  # 公士

# The results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation:
1. **Weights (衰):** The weights are assigned based on the rank, with higher ranks having smaller weights (e.g., 大夫 = 1) and lower ranks having larger weights (e.g., 公士 = 5).
2. **Reversed Weights (返衰之):** The weights are reversed by taking their reciprocal.
3. **Sum of Reversed Weights (副并为法):** The sum of the reversed weights is calculated to normalize the distribution.
4. **Calculate Contributions:** Each rank's contribution is proportional to its reversed weight divided by the total reversed weight, multiplied by the total money (100 coins).

### Output:
The variables `a`, `b`, `c`, `d`, and `e` will contain the amounts of money contributed by 大夫, 不更, 簪褭, 上造, and 公士, respectively, as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 1200/137, Actual: 6000/137
Variable 'b' has wrong value. Expected: 1500/137, Actual: 3000/137
Variable 'd' has wrong value. Expected: 3000/137, Actual: 1500/137
Variable 'e' has wrong value. Expected: 6000/137, Actual: 1200/137"""
