"""
今有率戸出絹三疋依貧富欲以九等出之令戸各差除二丈今有上上三十九戸上中二十四戸上下五十七戸中上三十一戸中中七十八戸中下四十三戸下上二十五戸下中七十六戸下下一十三戸問九等戸各應出絹㡬何
術曰置上八等戸各求積差上上戸十六上中戸十四上下戸十二中上戸十中中戸八中下戸六下上戸四下中戸二各以其戸數乗而併之以出絹疋丈數乗凡戸所得以併數減之餘以凡戸數而一所得即下下戸遞加差各得上八等戸所出絹疋丈數
答曰上上戸戸出絹 a疋 上中戸戸出絹 b疋 上下戸戸出絹 c疋 中上戸戸出絹 d疋 中中戸戸出絹 e疋 中下戸戸出絹 f疋 下上戸戸出絹 g疋 下中戸戸出絹 h疋 下下戸戸出絹 i疋
"""

#----- content starts here -----
"""
Suppose there is a tax rate of 3 bolts of silk per household. Based on wealth, it is desired to distribute the tax across 9 classes of households, with a difference of 2 zhang between each class.

There are:
- 39 households in the topmost class (上上),
- 24 households in the second class (上中),
- 57 households in the third class (上下),
- 31 households in the fourth class (中上),
- 78 households in the fifth class (中中),
- 43 households in the sixth class (中下),
- 25 households in the seventh class (下上),
- 76 households in the eighth class (下中),
- 13 households in the bottommost class (下下).

Question: How much silk does each household in each class contribute?

The procedure says:
1. Assign the differences for each class:
   - 上上戶 contributes 16,
   - 上中戶 contributes 14,
   - 上下戶 contributes 12,
   - 中上戶 contributes 10,
   - 中中戶 contributes 8,
   - 中下戶 contributes 6,
   - 下上戶 contributes 4,
   - 下中戶 contributes 2,
   - 下下戶 contributes 0.
2. Multiply the number of households in each class by their respective contribution, and sum these products to find the total contribution.
3. Multiply the total number of households by the tax rate (3 bolts of silk) to find the total silk required.
4. Subtract the total contribution from the total silk required. Divide the remainder by the total number of households to find the base contribution for the bottommost class (下下戶).
5. Add the difference for each class to the base contribution to find the contribution for each class.

Answer:
- Each 上上戶 contributes *a* bolts of silk,
- Each 上中戶 contributes *b* bolts of silk,
- Each 上下戶 contributes *c* bolts of silk,
- Each 中上戶 contributes *d* bolts of silk,
- Each 中中戶 contributes *e* bolts of silk,
- Each 中下戶 contributes *f* bolts of silk,
- Each 下上戶 contributes *g* bolts of silk,
- Each 下中戶 contributes *h* bolts of silk,
- Each 下下戶 contributes *i* bolts of silk.
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

# Contribution differences for each class
上上差 = 16
上中差 = 14
上下差 = 12
中上差 = 10
中中差 = 8
中下差 = 6
下上差 = 4
下中差 = 2
下下差 = 0

# Tax rate per household
稅率 = 3

# Step 1: Calculate the total contribution difference
積差 = (
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
總絹疋 = 總戶數 * 稅率

# Step 3: Calculate the base contribution for 下下戶
餘額 = 總絹疋 - 積差
下下戶貢獻 = Fraction(餘額, 總戶數)

# Step 4: Calculate the contribution for each class
a = 下下戶貢獻 + 上上差
b = 下下戶貢獻 + 上中差
c = 下下戶貢獻 + 上下差
d = 下下戶貢獻 + 中上差
e = 下下戶貢獻 + 中中差
f = 下下戶貢獻 + 中下差
g = 下下戶貢獻 + 下上差
h = 下下戶貢獻 + 下中差
i = 下下戶貢獻 + 下下差#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5, Actual: 11
Variable 'b' has wrong value. Expected: 9/2, Actual: 9
Variable 'c' has wrong value. Expected: 4, Actual: 7
Variable 'd' has wrong value. Expected: 7/2, Actual: 5
Variable 'f' has wrong value. Expected: 5/2, Actual: 1
Variable 'g' has wrong value. Expected: 2, Actual: -1
Variable 'h' has wrong value. Expected: 3/2, Actual: -3
Variable 'i' has wrong value. Expected: 1, Actual: -5"""
