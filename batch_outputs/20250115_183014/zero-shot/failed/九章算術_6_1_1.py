"""
今有均輸卒：甲縣一千二百人，薄塞；乙縣一千五百五十人，行道一日；丙縣一千二百八十人，行道二日；丁縣九百九十人，行道三日；戊縣一千七百五十人，行道五日。凡五縣，賦輸卒一月一千二百人。欲以遠近、戶率，多少衰出之。問︰縣各幾何？
術曰：令縣卒，各如其居所及行道日數而一，以為衰。甲衰四，乙衰五，丙衰四，丁衰三，戊衰五，副并為法。以人數乘未并者各自為實。實如法而一。有分者，上下輩之。
荅曰：甲縣 a人 。乙縣 b人 。丙縣 c人 。丁縣 d人 。戊縣 e人 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The solution involves calculating the number of soldiers (a, b, c, d, e) assigned to each county based on the given conditions.

Here is the Python code:


"""


from fractions import Fraction

# Given data
total_soldiers = 1200  # Total soldiers per month
weights = [4, 5, 4, 3, 5]  # Weights for each county (甲, 乙, 丙, 丁, 戊)
population = [1200, 1550, 1280, 990, 1750]  # Population of each county

# Calculate the total weight
total_weight = sum(weights)

# Calculate the number of soldiers assigned to each county
a = Fraction(weights[0] * total_soldiers, total_weight)
b = Fraction(weights[1] * total_soldiers, total_weight)
c = Fraction(weights[2] * total_soldiers, total_weight)
d = Fraction(weights[3] * total_soldiers, total_weight)
e = Fraction(weights[4] * total_soldiers, total_weight)

# Output the results
a, b, c, d, e


"""


### Explanation:
1. **Weights**: The weights are derived from the "衰" values mentioned in the problem (甲衰4, 乙衰5, 丙衰4, 丁衰3, 戊衰5).
2. **Total Weight**: The sum of all weights is calculated to distribute the total soldiers proportionally.
3. **Proportional Distribution**: Each county's share of soldiers is calculated as `(weight of the county * total soldiers) / total weight`.
4. **Fraction**: The `Fraction` class is used to ensure precise calculations, especially for non-integer results.

### Results:
The variables `a`, `b`, `c`, `d`, and `e` represent the number of soldiers assigned to counties 甲, 乙, 丙, 丁, and 戊, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 229, Actual: 1600/7
Variable 'b' has wrong value. Expected: 286, Actual: 2000/7
Variable 'c' has wrong value. Expected: 228, Actual: 1600/7
Variable 'd' has wrong value. Expected: 171, Actual: 1200/7
Variable 'e' has wrong value. Expected: 286, Actual: 2000/7"""
