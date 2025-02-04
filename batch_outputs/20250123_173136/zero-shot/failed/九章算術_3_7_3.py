"""
今有大夫、不更、簪褭、上造、公士，凡五人，共出百錢。欲令高爵出少，以次漸多，問︰各幾何？
返衰術曰：列置衰而令相乘，動者為不動者衰。術曰：置爵數各自為衰，而返衰之，副并為法。以百錢乘未并者各自為實。實如法得一錢。
荅曰：大夫出 a錢 。不更出 b錢 。簪褭出 c錢 。上造出 d錢 。公士出 e錢 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical method into Python code. The problem involves distributing 100 coins among five ranks (大夫, 不更, 簪褭, 上造, 公士) such that higher ranks contribute fewer coins, and the contributions increase progressively for lower ranks.

The solution involves using the "返衰術" (reversal of proportions) method. Here's the Python code:


"""


from fractions import Fraction

# Define the ranks' weights (proportions) in reverse order
# 公士: 1, 上造: 2, 簪褭: 3, 不更: 4, 大夫: 5
weights = [5, 4, 3, 2, 1]

# Calculate the total weight
total_weight = sum(weights)

# Total coins to be distributed
total_coins = 100

# Calculate the amount each rank contributes
a = Fraction(weights[0], total_weight) * total_coins  # 大夫
b = Fraction(weights[1], total_weight) * total_coins  # 不更
c = Fraction(weights[2], total_weight) * total_coins  # 簪褭
d = Fraction(weights[3], total_weight) * total_coins  # 上造
e = Fraction(weights[4], total_weight) * total_coins  # 公士

# The results are stored in variables a, b, c, d, e


"""


### Explanation:
1. **Weights**: The ranks are assigned weights in reverse order of their hierarchy (higher ranks have larger weights).
2. **Total Weight**: The sum of all weights is calculated.
3. **Proportional Distribution**: Each rank's contribution is calculated as a fraction of the total coins, proportional to its weight.

### Results:
The variables `a`, `b`, `c`, `d`, and `e` represent the contributions of 大夫, 不更, 簪褭, 上造, and 公士, respectively. These are expressed as fractions for precision.
"""


"""
Variable 'a' has wrong value. Expected: 1200/137, Actual: 100/3
Variable 'b' has wrong value. Expected: 1500/137, Actual: 80/3
Variable 'c' has wrong value. Expected: 2000/137, Actual: 20
Variable 'd' has wrong value. Expected: 3000/137, Actual: 40/3
Variable 'e' has wrong value. Expected: 6000/137, Actual: 20/3"""
