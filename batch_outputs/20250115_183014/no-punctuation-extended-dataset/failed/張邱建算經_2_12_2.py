"""
今有率戸出絹三疋依貧富欲以九等出之令戸各差除二丈今有上上三十九戸上中二十四戸上下五十七戸中上三十一戸中中七十八戸中下四十三戸下上二十五戸下中七十六戸下下一十三戸問九等戸各應出絹㡬何
術曰置上八等戸各求積差上上戸十六上中戸十四上下戸十二中上戸十中中戸八中下戸六下上戸四下中戸二各以其戸數乗而併之以出絹疋丈數乗凡戸所得以併數減之餘以凡戸數而一所得即下下戸遞加差各得上八等戸所出絹疋丈數
答曰上上戸戸出絹 a疋 上中戸戸出絹 b疋 c 大上下戸戸出絹 d疋 中上戸戸出絹 e疋 中中戸戸出絹 f疋 中下戸戸出絹 g疋 下上戸戸出絹 h疋 下中戸戸出絹 i疋 下下戸戸出絹 j疋
"""

"""
Suppose there is a tax rate where each household contributes 3 bolts of silk. Based on wealth, it is desired to divide the households into nine ranks, with each rank differing by 2 zhang (units of silk). 
The households are distributed as follows:
- Shangshang (upper-upper): 39 households
- Shangzhong (upper-middle): 24 households
- Shangxia (upper-lower): 57 households
- Zhongshang (middle-upper): 31 households
- Zhongzhong (middle-middle): 78 households
- Zhongxia (middle-lower): 43 households
- Xiashang (lower-upper): 25 households
- Xiazhong (lower-middle): 76 households
- Xiaxia (lower-lower): 13 households

Question: How much silk does each household in the nine ranks contribute?

The procedure says:
1. Assign the rank differences: Shangshang households contribute 16, Shangzhong 14, Shangxia 12, Zhongshang 10, Zhongzhong 8, Zhongxia 6, Xiashang 4, Xiazhong 2, and Xiaxia 0.
2. Multiply the number of households in each rank by their respective contribution rates and sum them to find the total contribution.
3. Multiply the total number of households by the base contribution (3 bolts per household) to find the expected total contribution.
4. Subtract the total contribution from the expected contribution to find the remainder.
5. Divide the remainder by the total number of households to find the adjustment per household.
6. Add the adjustment to the base contribution for each rank, starting from the lowest rank (Xiaxia), and incrementally add the rank differences.

Answer:
- Shangshang households contribute *a* bolts of silk.
- Shangzhong households contribute *b* bolts and *c* zhang of silk.
- Shangxia households contribute *d* bolts of silk.
- Zhongshang households contribute *e* bolts of silk.
- Zhongzhong households contribute *f* bolts of silk.
- Zhongxia households contribute *g* bolts of silk.
- Xiashang households contribute *h* bolts of silk.
- Xiazhong households contribute *i* bolts of silk.
- Xiaxia households contribute *j* bolts of silk.
"""

from fractions import Fraction

# Number of households in each rank
households = {
    "Shangshang": 39,
    "Shangzhong": 24,
    "Shangxia": 57,
    "Zhongshang": 31,
    "Zhongzhong": 78,
    "Zhongxia": 43,
    "Xiashang": 25,
    "Xiazhong": 76,
    "Xiaxia": 13,
}

# Contribution rates for each rank
rates = {
    "Shangshang": 16,
    "Shangzhong": 14,
    "Shangxia": 12,
    "Zhongshang": 10,
    "Zhongzhong": 8,
    "Zhongxia": 6,
    "Xiashang": 4,
    "Xiazhong": 2,
    "Xiaxia": 0,
}

# Base contribution per household
base_contribution = 3

# Step 1: Calculate the total contribution based on rank differences
total_contribution = sum(households[rank] * rates[rank] for rank in households)

# Step 2: Calculate the expected total contribution
total_households = sum(households.values())
expected_contribution = total_households * base_contribution

# Step 3: Calculate the remainder
remainder = expected_contribution - total_contribution

# Step 4: Calculate the adjustment per household
adjustment_per_household = Fraction(remainder, total_households)

# Step 5: Calculate the contribution for each rank
rank_contributions = {}
current_contribution = adjustment_per_household  # Start with the adjustment for the lowest rank
for rank in reversed(list(rates.keys())):  # Start from the lowest rank
    rank_contributions[rank] = current_contribution
    current_contribution += Fraction(rates[rank], 1)

# Extract contributions for each rank
a = rank_contributions["Shangshang"]
b = rank_contributions["Shangzhong"].numerator // rank_contributions["Shangzhong"].denominator
c = rank_contributions["Shangzhong"] - b
d = rank_contributions["Shangxia"]
e = rank_contributions["Zhongshang"]
f = rank_contributions["Zhongzhong"]
g = rank_contributions["Zhongxia"]
h = rank_contributions["Xiashang"]
i = rank_contributions["Xiazhong"]
j = rank_contributions["Xiaxia"]
"""
Variable 'a' has wrong value. Expected: 5, Actual: 51
Variable 'b' has wrong value. Expected: 4, Actual: 37
Variable 'c' has wrong value. Expected: 2, Actual: 0
Variable 'd' has wrong value. Expected: 4, Actual: 25
Variable 'e' has wrong value. Expected: 7/2, Actual: 15
Variable 'f' has wrong value. Expected: 3, Actual: 7
Variable 'g' has wrong value. Expected: 5/2, Actual: 1
Variable 'h' has wrong value. Expected: 2, Actual: -3
Variable 'i' has wrong value. Expected: 3/2, Actual: -5
Variable 'j' has wrong value. Expected: 1, Actual: -5"""
