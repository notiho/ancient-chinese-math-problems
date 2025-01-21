"""
今有率戸出絹三疋依貧富欲以九等出之令戸各差除二丈今有上上三十九戸上中二十四戸上下五十七戸中上三十一戸中中七十八戸中下四十三戸下上二十五戸下中七十六戸下下一十三戸問九等戸各應出絹㡬何
術曰置上八等戸各求積差上上戸十六上中戸十四上下戸十二中上戸十中中戸八中下戸六下上戸四下中戸二各以其戸數乗而併之以出絹疋丈數乗凡戸所得以併數減之餘以凡戸數而一所得即下下戸遞加差各得上八等戸所出絹疋丈數
答曰上上戸戸出絹 a疋 上中戸戸出絹 b疋 c 大上下戸戸出絹 d疋 中上戸戸出絹 e疋 中中戸戸出絹 f疋 中下戸戸出絹 g疋 下上戸戸出絹 h疋 下中戸戸出絹 i疋 下下戸戸出絹 j疋
"""

"""
Suppose there is a tax rate of 3 bolts of silk per household, adjusted according to wealth into 9 grades. Each household differs by 2 zhang (units of silk). 
The number of households in each grade is as follows:
- Upper Upper: 39 households
- Upper Middle: 24 households
- Upper Lower: 57 households
- Middle Upper: 31 households
- Middle Middle: 78 households
- Middle Lower: 43 households
- Lower Upper: 25 households
- Lower Middle: 76 households
- Lower Lower: 13 households

Question: How much silk should each household in the 9 grades contribute?

The procedure says:
1. Assign the grade differences as follows:
   - Upper Upper: 16
   - Upper Middle: 14
   - Upper Lower: 12
   - Middle Upper: 10
   - Middle Middle: 8
   - Middle Lower: 6
   - Lower Upper: 4
   - Lower Middle: 2
   - Lower Lower: 0
2. Multiply the number of households in each grade by their respective grade difference, and sum these to calculate the total contribution.
3. Multiply the total number of households by the base contribution (3 bolts of silk per household), and subtract the total contribution calculated in step 2.
4. Divide the remainder by the total number of households to find the base contribution for the lowest grade (Lower Lower).
5. Add the grade differences to the base contribution to calculate the contribution for each grade.

Answer:
- Upper Upper households contribute *a* bolts of silk each.
- Upper Middle households contribute *b* bolts of silk each.
- Upper Lower households contribute *c* bolts of silk each.
- Middle Upper households contribute *d* bolts of silk each.
- Middle Middle households contribute *e* bolts of silk each.
- Middle Lower households contribute *f* bolts of silk each.
- Lower Upper households contribute *g* bolts of silk each.
- Lower Middle households contribute *h* bolts of silk each.
- Lower Lower households contribute *i* bolts of silk each.
"""

# Number of households in each grade
戶數 = {
    "上上": 39,
    "上中": 24,
    "上下": 57,
    "中上": 31,
    "中中": 78,
    "中下": 43,
    "下上": 25,
    "下中": 76,
    "下下": 13
}

# Grade differences
差 = {
    "上上": 16,
    "上中": 14,
    "上下": 12,
    "中上": 10,
    "中中": 8,
    "中下": 6,
    "下上": 4,
    "下中": 2,
    "下下": 0
}

# Base contribution per household (3 bolts of silk)
基準出絹 = 3

# Step 1: Calculate the total contribution difference
總差積 = sum(戶數[grade] * 差[grade] for grade in 戶數)

# Step 2: Calculate the total contribution based on the base rate
總基準出絹 = sum(戶數.values()) * 基準出絹

# Step 3: Calculate the remainder after subtracting the total contribution difference
餘額 = 總基準出絹 - 總差積

# Step 4: Calculate the base contribution for the lowest grade (下下)
下下出絹 = Fraction(餘額, sum(戶數.values()))

# Step 5: Calculate the contribution for each grade
出絹 = {grade: 下下出絹 + Fraction(差[grade], 1) for grade in 戶數}

# Assign results to variables
a = 出絹["上上"]
b = 出絹["上中"]
c = 出絹["上下"]
d = 出絹["中上"]
e = 出絹["中中"]
f = 出絹["中下"]
g = 出絹["下上"]
h = 出絹["下中"]
i = 出絹["下下"]
"""
Variable 'a' has wrong value. Expected: 5, Actual: 11
Variable 'b' has wrong value. Expected: 4, Actual: 9
Variable 'c' has wrong value. Expected: 2, Actual: 7
Variable 'd' has wrong value. Expected: 4, Actual: 5
Variable 'e' has wrong value. Expected: 7/2, Actual: 3
Variable 'f' has wrong value. Expected: 3, Actual: 1
Variable 'g' has wrong value. Expected: 5/2, Actual: -1
Variable 'h' has wrong value. Expected: 2, Actual: -3
Variable 'i' has wrong value. Expected: 3/2, Actual: -5
Missing variable in output: 'j'"""
