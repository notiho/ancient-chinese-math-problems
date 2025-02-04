"""
今有率戸出絹三疋依貧富欲以九等出之令戸各差除二丈今有上上三十九戸上中二十四戸上下五十七戸中上三十一戸中中七十八戸中下四十三戸下上二十五戸下中七十六戸下下一十三戸問九等戸各應出絹㡬何
術曰置上八等戸各求積差上上戸十六上中戸十四上下戸十二中上戸十中中戸八中下戸六下上戸四下中戸二各以其戸數乗而併之以出絹疋丈數乗凡戸所得以併數減之餘以凡戸數而一所得即下下戸遞加差各得上八等戸所出絹疋丈數
答曰上上戸戸出絹 a疋 上中戸戸出絹 b疋 上下戸戸出絹 c疋 中上戸戸出絹 d疋 中中戸戸出絹 e疋 中下戸戸出絹 f疋 下上戸戸出絹 g疋 下中戸戸出絹 h疋 下下戸戸出絹 i疋
"""

"""
Suppose there is a tax rate of 3 bolts of silk per household. Based on wealth, it is desired to distribute the tax across 9 classes of households, with each class differing by 2 zhang (units of silk). 
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

Question: How much silk should each household in the 9 classes contribute?

The procedure says:
1. Assign the differences for each class:
   - Shangshang households: 16
   - Shangzhong households: 14
   - Shangxia households: 12
   - Zhongshang households: 10
   - Zhongzhong households: 8
   - Zhongxia households: 6
   - Xiashang households: 4
   - Xiazhong households: 2
   - Xiaxia households: 0
2. Multiply the number of households in each class by their respective differences, and sum these products to obtain the total weighted difference.
3. Multiply the total number of households by the tax rate (3 bolts of silk) to get the total silk required.
4. Subtract the total weighted difference from the total silk required.
5. Divide the remainder by the total number of households to determine the base contribution for the lowest class (Xiaxia).
6. Add the respective differences to the base contribution to calculate the silk contribution for each class.

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

# Differences for each class
上上差 = 16
上中差 = 14
上下差 = 12
中上差 = 10
中中差 = 8
中下差 = 6
下上差 = 4
下中差 = 2
下下差 = 0

# Tax rate (silk per household)
稅率 = 3

# Step 1: Calculate the total weighted difference
總差積 = (
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
總絹數 = 總戶數 * 稅率

# Step 3: Subtract the total weighted difference from the total silk required
餘絹數 = 總絹數 - 總差積

# Step 4: Calculate the base contribution for the lowest class (Xiaxia)
下下戶出絹 = Fraction(餘絹數, 總戶數)

# Step 5: Calculate the silk contribution for each class
上上戶出絹 = 下下戶出絹 + Fraction(上上差, 總戶數)
上中戶出絹 = 下下戶出絹 + Fraction(上中差, 總戶數)
上下戶出絹 = 下下戶出絹 + Fraction(上下差, 總戶數)
中上戶出絹 = 下下戶出絹 + Fraction(中上差, 總戶數)
中中戶出絹 = 下下戶出絹 + Fraction(中中差, 總戶數)
中下戶出絹 = 下下戶出絹 + Fraction(中下差, 總戶數)
下上戶出絹 = 下下戶出絹 + Fraction(下上差, 總戶數)
下中戶出絹 = 下下戶出絹 + Fraction(下中差, 總戶數)

# Assign results to variables
a = 上上戶出絹
b = 上中戶出絹
c = 上下戶出絹
d = 中上戶出絹
e = 中中戶出絹
f = 中下戶出絹
g = 下上戶出絹
h = 下中戶出絹
i = 下下戶出絹
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
