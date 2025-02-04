"""
今有率戸出絹三疋依貧富欲以九等出之令戸各差除二丈今有上上三十九戸上中二十四戸上下五十七戸中上三十一戸中中七十八戸中下四十三戸下上二十五戸下中七十六戸下下一十三戸問九等戸各應出絹㡬何
術曰置上八等戸各求積差上上戸十六上中戸十四上下戸十二中上戸十中中戸八中下戸六下上戸四下中戸二各以其戸數乗而併之以出絹疋丈數乗凡戸所得以併數減之餘以凡戸數而一所得即下下戸遞加差各得上八等戸所出絹疋丈數
答曰上上戸戸出絹 a疋 上中戸戸出絹 b疋 上下戸戸出絹 c疋 中上戸戸出絹 d疋 中中戸戸出絹 e疋 中下戸戸出絹 f疋 下上戸戸出絹 g疋 下中戸戸出絹 h疋 下下戸戸出絹 i疋
"""

"""
Suppose there is a tax rate of 3 bolts of silk per household. Based on wealth, it is desired to distribute the tax across 9 classes of households, with each class differing by 2 zhang (units of silk).

The households are divided as follows:
- Shang Shang (上上): 39 households
- Shang Zhong (上中): 24 households
- Shang Xia (上下): 57 households
- Zhong Shang (中上): 31 households
- Zhong Zhong (中中): 78 households
- Zhong Xia (中下): 43 households
- Xia Shang (下上): 25 households
- Xia Zhong (下中): 76 households
- Xia Xia (下下): 13 households

Question: How much silk should each household in each of the 9 classes pay?

The procedure says:
1. Assign the differences in tax for each class:
   - Shang Shang households: 16
   - Shang Zhong households: 14
   - Shang Xia households: 12
   - Zhong Shang households: 10
   - Zhong Zhong households: 8
   - Zhong Xia households: 6
   - Xia Shang households: 4
   - Xia Zhong households: 2
   - Xia Xia households: 0
2. Multiply the number of households in each class by their respective tax difference, and sum these products to get the total weighted tax difference.
3. Multiply the total number of households by the base tax rate (3 bolts of silk) to get the total tax in bolts.
4. Subtract the total weighted tax difference from the total tax, and divide the remainder by the total number of households to get the base tax for the lowest class (Xia Xia).
5. Add the tax differences to the base tax to calculate the tax for each class.

Answer:
- Shang Shang households pay *a* bolts of silk each.
- Shang Zhong households pay *b* bolts of silk each.
- Shang Xia households pay *c* bolts of silk each.
- Zhong Shang households pay *d* bolts of silk each.
- Zhong Zhong households pay *e* bolts of silk each.
- Zhong Xia households pay *f* bolts of silk each.
- Xia Shang households pay *g* bolts of silk each.
- Xia Zhong households pay *h* bolts of silk each.
- Xia Xia households pay *i* bolts of silk each.
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

# Tax differences for each class
上上差 = 16
上中差 = 14
上下差 = 12
中上差 = 10
中中差 = 8
中下差 = 6
下上差 = 4
下中差 = 2
下下差 = 0

# Base tax rate (3 bolts of silk per household)
基準稅率 = 3

# Step 1: Calculate the total weighted tax difference
總差數 = (
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

# Step 2: Calculate the total number of households
總戶數 = (
    上上戶 + 上中戶 + 上下戶 +
    中上戶 + 中中戶 + 中下戶 +
    下上戶 + 下中戶 + 下下戶
)

# Step 3: Calculate the total tax in bolts
總稅疋 = 總戶數 * 基準稅率

# Step 4: Calculate the base tax for the lowest class (Xia Xia)
下下稅 = Fraction(總稅疋 - 總差數, 總戶數)

# Step 5: Calculate the tax for each class
上上稅 = 下下稅 + Fraction(上上差, 總戶數)
上中稅 = 下下稅 + Fraction(上中差, 總戶數)
上下稅 = 下下稅 + Fraction(上下差, 總戶數)
中上稅 = 下下稅 + Fraction(中上差, 總戶數)
中中稅 = 下下稅 + Fraction(中中差, 總戶數)
中下稅 = 下下稅 + Fraction(中下差, 總戶數)
下上稅 = 下下稅 + Fraction(下上差, 總戶數)
下中稅 = 下下稅 + Fraction(下中差, 總戶數)
下下稅 = 下下稅 + Fraction(下下差, 總戶數)

# Assign results
a = 上上稅
b = 上中稅
c = 上下稅
d = 中上稅
e = 中中稅
f = 中下稅
g = 下上稅
h = 下中稅
i = 下下稅
"""
Variable 'a' has wrong value. Expected: 5, Actual: -957/193
Variable 'b' has wrong value. Expected: 9/2, Actual: -958/193
Variable 'c' has wrong value. Expected: 4, Actual: -959/193
Variable 'd' has wrong value. Expected: 7/2, Actual: -960/193
Variable 'e' has wrong value. Expected: 3, Actual: -961/193
Variable 'f' has wrong value. Expected: 5/2, Actual: -962/193
Variable 'g' has wrong value. Expected: 2, Actual: -963/193
Variable 'h' has wrong value. Expected: 3/2, Actual: -964/193
Variable 'i' has wrong value. Expected: 1, Actual: -5"""
