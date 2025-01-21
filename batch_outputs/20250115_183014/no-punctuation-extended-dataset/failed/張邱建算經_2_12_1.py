"""
今有率戸出絹三疋依貧富欲以九等出之令戸各差除二丈今有上上三十九戸上中二十四戸上下五十七戸中上三十一戸中中七十八戸中下四十三戸下上二十五戸下中七十六戸下下一十三戸問九等戸各應出絹㡬何
術曰置上八等戸各求積差上上戸十六上中戸十四上下戸十二中上戸十中中戸八中下戸六下上戸四下中戸二各以其戸數乗而併之以出絹疋丈數乗凡戸所得以併數減之餘以凡戸數而一所得即下下戸遞加差各得上八等戸所出絹疋丈數
答曰上上戸戸出絹 a疋 上中戸戸出絹 b疋 c 大上下戸戸出絹 d疋 中上戸戸出絹 e疋 中中戸戸出絹 f疋 中下戸戸出絹 g疋 下上戸戸出絹 h疋 下中戸戸出絹 i疋 下下戸戸出絹 j疋
"""

"""
Suppose there is a tax rate where each household is to contribute 3 bolts of silk. Based on wealth, it is desired to divide the contribution into nine classes, with each class differing by 2 zhang (units of length).

The households are distributed as follows:
- Shang Shang (Upper Upper): 39 households
- Shang Zhong (Upper Middle): 24 households
- Shang Xia (Upper Lower): 57 households
- Zhong Shang (Middle Upper): 31 households
- Zhong Zhong (Middle Middle): 78 households
- Zhong Xia (Middle Lower): 43 households
- Xia Shang (Lower Upper): 25 households
- Xia Zhong (Lower Middle): 76 households
- Xia Xia (Lower Lower): 13 households

Question: How much silk should each household in the nine classes contribute?

The procedure says:
1. Assign the weights for each class:
   - Shang Shang: 16
   - Shang Zhong: 14
   - Shang Xia: 12
   - Zhong Shang: 10
   - Zhong Zhong: 8
   - Zhong Xia: 6
   - Xia Shang: 4
   - Xia Zhong: 2
   - Xia Xia: 0
2. Multiply the number of households in each class by their respective weights, and sum these products to get the total weighted contribution.
3. Multiply the total number of households by the base contribution (3 bolts of silk) to get the total silk required.
4. Subtract the total weighted contribution from the total silk required. Divide the remainder by the total number of households to get the base contribution for the lowest class (Xia Xia).
5. Add the difference (2 zhang) progressively for each higher class to determine the contribution for each class.

Answer:
- Shang Shang households contribute *a* bolts of silk each.
- Shang Zhong households contribute *b* bolts and *c* zhang each.
- Shang Xia households contribute *d* bolts of silk each.
- Zhong Shang households contribute *e* bolts of silk each.
- Zhong Zhong households contribute *f* bolts of silk each.
- Zhong Xia households contribute *g* bolts of silk each.
- Xia Shang households contribute *h* bolts of silk each.
- Xia Zhong households contribute *i* bolts of silk each.
- Xia Xia households contribute *j* bolts of silk each.
"""

# Number of households in each class
households = {
    "ShangShang": 39,
    "ShangZhong": 24,
    "ShangXia": 57,
    "ZhongShang": 31,
    "ZhongZhong": 78,
    "ZhongXia": 43,
    "XiaShang": 25,
    "XiaZhong": 76,
    "XiaXia": 13,
}

# Weights for each class
weights = {
    "ShangShang": 16,
    "ShangZhong": 14,
    "ShangXia": 12,
    "ZhongShang": 10,
    "ZhongZhong": 8,
    "ZhongXia": 6,
    "XiaShang": 4,
    "XiaZhong": 2,
    "XiaXia": 0,
}

# Base contribution per household
base_contribution = 3

# Step 1: Calculate the total weighted contribution
total_weighted_contribution = sum(
    households[class_name] * weights[class_name] for class_name in households
)

# Step 2: Calculate the total silk required
total_households = sum(households.values())
total_silk_required = total_households * base_contribution

# Step 3: Calculate the base contribution for the lowest class (Xia Xia)
remainder = total_silk_required - total_weighted_contribution
base_contribution_xiaxia = Fraction(remainder, total_households)

# Step 4: Calculate contributions for each class
contributions = {}
for class_name in weights:
    contributions[class_name] = base_contribution_xiaxia + Fraction(weights[class_name], 2)

# Assign contributions to variables
a = contributions["ShangShang"]
b = contributions["ShangZhong"].numerator // contributions["ShangZhong"].denominator
c = contributions["ShangZhong"] - b
d = contributions["ShangXia"]
e = contributions["ZhongShang"]
f = contributions["ZhongZhong"]
g = contributions["ZhongXia"]
h = contributions["XiaShang"]
i = contributions["XiaZhong"]
j = contributions["XiaXia"]
"""
Variable 'a' has wrong value. Expected: 5, Actual: 3
Variable 'b' has wrong value. Expected: 4, Actual: 2
Variable 'c' has wrong value. Expected: 2, Actual: 0
Variable 'd' has wrong value. Expected: 4, Actual: 1
Variable 'e' has wrong value. Expected: 7/2, Actual: 0
Variable 'f' has wrong value. Expected: 3, Actual: -1
Variable 'g' has wrong value. Expected: 5/2, Actual: -2
Variable 'h' has wrong value. Expected: 2, Actual: -3
Variable 'i' has wrong value. Expected: 3/2, Actual: -4
Variable 'j' has wrong value. Expected: 1, Actual: -5"""
