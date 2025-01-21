"""
今有率戸出絹三疋依貧富欲以九等出之令戸各差除二丈今有上上三十九戸上中二十四戸上下五十七戸中上三十一戸中中七十八戸中下四十三戸下上二十五戸下中七十六戸下下一十三戸問九等戸各應出絹㡬何
術曰置上八等戸各求積差上上戸十六上中戸十四上下戸十二中上戸十中中戸八中下戸六下上戸四下中戸二各以其戸數乗而併之以出絹疋丈數乗凡戸所得以併數減之餘以凡戸數而一所得即下下戸遞加差各得上八等戸所出絹疋丈數
答曰上上戸戸出絹 a疋 上中戸戸出絹 b疋 c 大上下戸戸出絹 d疋 中上戸戸出絹 e疋 中中戸戸出絹 f疋 中下戸戸出絹 g疋 下上戸戸出絹 h疋 下中戸戸出絹 i疋 下下戸戸出絹 j疋
"""

"""
Suppose there is a tax rate of 3 bolts of silk per household, adjusted according to wealth into nine ranks. Each rank differs by 2 zhang (20 chi). 
There are:
- 39 households in the highest rank (上上),
- 24 households in the second-highest rank (上中),
- 57 households in the third rank (上下),
- 31 households in the fourth rank (中上),
- 78 households in the fifth rank (中中),
- 43 households in the sixth rank (中下),
- 25 households in the seventh rank (下上),
- 76 households in the eighth rank (下中),
- 13 households in the lowest rank (下下).

Question: How much silk does each household in each rank contribute?

The procedure says:
1. Assign the rank multipliers: 上上 households are 16, 上中 are 14, 上下 are 12, 中上 are 10, 中中 are 8, 中下 are 6, 下上 are 4, 下中 are 2, and 下下 are 0.
2. Multiply the number of households in each rank by their respective multipliers and sum these to get the total weighted contribution.
3. Multiply the total number of households by the base tax rate (3 bolts of silk) to get the total silk required.
4. Subtract the total weighted contribution from the total silk required.
5. Divide the remainder by the total number of households to get the base contribution for the lowest rank (下下).
6. Add the rank differences (2 zhang per rank) to the base contribution to calculate the contribution for each rank.

Answer: Each household in each rank contributes:
- 上上戶戶出絹 *a* bolts,
- 上中戶戶出絹 *b* bolts,
- 上下戶戶出絹 *c* bolts,
- 中上戶戶出絹 *d* bolts,
- 中中戶戶出絹 *e* bolts,
- 中下戶戶出絹 *f* bolts,
- 下上戶戶出絹 *g* bolts,
- 下中戶戶出絹 *h* bolts,
- 下下戶戶出絹 *i* bolts.
"""

# 戶數 for each rank
戶數 = {
    "上上": 39,
    "上中": 24,
    "上下": 57,
    "中上": 31,
    "中中": 78,
    "中下": 43,
    "下上": 25,
    "下中": 76,
    "下下": 13,
}

# 差 for each rank
差 = {
    "上上": 16,
    "上中": 14,
    "上下": 12,
    "中上": 10,
    "中中": 8,
    "中下": 6,
    "下上": 4,
    "下中": 2,
    "下下": 0,
}

# Base tax rate (絹 per 戶)
基準絹 = 3

# Step 1: Calculate the total weighted contribution
總積差 = sum(戶數[rank] * 差[rank] for rank in 戶數)

# Step 2: Calculate the total silk required
總戶數 = sum(戶數.values())
總絹 = 總戶數 * 基準絹

# Step 3: Calculate the base contribution for the lowest rank (下下)
餘額 = 總絹 - 總積差
下下戶絹 = Fraction(餘額, 總戶數)

# Step 4: Calculate the contribution for each rank
戶出絹 = {rank: 下下戶絹 + Fraction(差[rank], 10) for rank in 戶數}

# Extract results
a = 戶出絹["上上"]
b = 戶出絹["上中"]
c = 戶出絹["上下"]
d = 戶出絹["中上"]
e = 戶出絹["中中"]
f = 戶出絹["中下"]
g = 戶出絹["下上"]
h = 戶出絹["下中"]
i = 戶出絹["下下"]
"""
Variable 'a' has wrong value. Expected: 5, Actual: -17/5
Variable 'b' has wrong value. Expected: 4, Actual: -18/5
Variable 'c' has wrong value. Expected: 2, Actual: -19/5
Variable 'd' has wrong value. Expected: 4, Actual: -4
Variable 'e' has wrong value. Expected: 7/2, Actual: -21/5
Variable 'f' has wrong value. Expected: 3, Actual: -22/5
Variable 'g' has wrong value. Expected: 5/2, Actual: -23/5
Variable 'h' has wrong value. Expected: 2, Actual: -24/5
Variable 'i' has wrong value. Expected: 3/2, Actual: -5
Missing variable in output: 'j'"""
