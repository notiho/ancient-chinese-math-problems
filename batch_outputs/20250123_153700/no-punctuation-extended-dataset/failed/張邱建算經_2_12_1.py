"""
今有率戸出絹三疋依貧富欲以九等出之令戸各差除二丈今有上上三十九戸上中二十四戸上下五十七戸中上三十一戸中中七十八戸中下四十三戸下上二十五戸下中七十六戸下下一十三戸問九等戸各應出絹㡬何
術曰置上八等戸各求積差上上戸十六上中戸十四上下戸十二中上戸十中中戸八中下戸六下上戸四下中戸二各以其戸數乗而併之以出絹疋丈數乗凡戸所得以併數減之餘以凡戸數而一所得即下下戸遞加差各得上八等戸所出絹疋丈數
答曰上上戸戸出絹 a疋 上中戸戸出絹 b疋 上下戸戸出絹 c疋 中上戸戸出絹 d疋 中中戸戸出絹 e疋 中下戸戸出絹 f疋 下上戸戸出絹 g疋 下中戸戸出絹 h疋 下下戸戸出絹 i疋
"""

"""
Suppose there is a tax rate of 3 bolts of silk per household. Based on wealth, it is desired to distribute the tax among nine classes of households, with a difference of 2 zhang between each class.

The households are divided as follows:
- Shangshang (upper-upper): 39 households
- Shangzhong (upper-middle): 24 households
- Shangxia (upper-lower): 57 households
- Zhongshang (middle-upper): 31 households
- Zhongzhong (middle-middle): 78 households
- Zhongxia (middle-lower): 43 households
- Xiashang (lower-upper): 25 households
- Xiazhong (lower-middle): 76 households
- Xiaxia (lower-lower): 13 households

Question: How much silk should each household in the nine classes contribute?

The procedure says:
1. Assign the weights (differences) for each class:
   - Shangshang: 16
   - Shangzhong: 14
   - Shangxia: 12
   - Zhongshang: 10
   - Zhongzhong: 8
   - Zhongxia: 6
   - Xiashang: 4
   - Xiazhong: 2
   - Xiaxia: 0
2. Multiply the number of households in each class by its weight, and sum these to get the total weighted contribution.
3. Multiply the total number of households by the tax rate (3 bolts of silk) to get the total silk required.
4. Divide the total silk required by the total weighted contribution to get the base contribution per weight unit.
5. For each class, multiply its weight by the base contribution to determine the silk contribution per household.

Answer:
- Shangshang households contribute *a* bolts of silk each.
- Shangzhong households contribute *b* bolts of silk each.
- Shangxia households contribute *c* bolts of silk each.
- Zhongshang households contribute *d* bolts of silk each.
- Zhongzhong households contribute *e* bolts of silk each.
- Zhongxia households contribute *f* bolts of silk each.
- Xiashang households contribute *g* bolts of silk each.
- Xiazhong households contribute *h* bolts of silk each.
- Xiaxia households contribute *i* bolts of silk each.
"""

# Number of households in each class
上上戶 = 39
上中戶 = 24
上下戶 = 57
中上戶 = 31
中中戶 = 78
中下戶 = 43
下上戶 = 25
下中戶 = 76
下下戶 = 13

# Weights (differences) for each class
上上差 = 16
上中差 = 14
上下差 = 12
中上差 = 10
中中差 = 8
中下差 = 6
下上差 = 4
下中差 = 2
下下差 = 0

# Tax rate (silk bolts per household)
稅率 = 3

# Step 1: Calculate the total weighted contribution
總加權 = (
    上上戶 * 上上差 +
    上中戶 * 上中差 +
    上下戶 * 上下差 +
    中上戶 * 中上差 +
    中中戶 * 中中差 +
    中下戶 * 中下差 +
    下上戶 * 下上差 +
    下中戶 * 下中差 +
    下下戶 * 下下差
)

# Step 2: Calculate the total silk required
總戶數 = 上上戶 + 上中戶 + 上下戶 + 中上戶 + 中中戶 + 中下戶 + 下上戶 + 下中戶 + 下下戶
總絹 = 總戶數 * 稅率

# Step 3: Calculate the base contribution per weight unit
基準貢獻 = Fraction(總絹, 總加權)

# Step 4: Calculate the silk contribution per household for each class
a = 上上差 * 基準貢獻
b = 上中差 * 基準貢獻
c = 上下差 * 基準貢獻
d = 中上差 * 基準貢獻
e = 中中差 * 基準貢獻
f = 中下差 * 基準貢獻
g = 下上差 * 基準貢獻
h = 下中差 * 基準貢獻
i = 下下差 * 基準貢獻
"""
Variable 'a' has wrong value. Expected: 5, Actual: 6
Variable 'b' has wrong value. Expected: 9/2, Actual: 21/4
Variable 'c' has wrong value. Expected: 4, Actual: 9/2
Variable 'd' has wrong value. Expected: 7/2, Actual: 15/4
Variable 'f' has wrong value. Expected: 5/2, Actual: 9/4
Variable 'g' has wrong value. Expected: 2, Actual: 3/2
Variable 'h' has wrong value. Expected: 3/2, Actual: 3/4
Variable 'i' has wrong value. Expected: 1, Actual: 0"""
