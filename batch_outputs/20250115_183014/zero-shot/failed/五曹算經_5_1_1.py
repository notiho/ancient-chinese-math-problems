"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
術曰：列絲八石五斤三两八銖，以四乘八石得三十二鈞；以三十斤乘之、納五斤，得九百六十五斤；以十六两乘之、納三两，得一萬五千四百四十三两；以二十四銖乘之、納八銖，得三十七萬六百四十銖。以五百六十五户除之，得一户六百五十六銖；以二十四銖除之，得二十七两奇八銖；以十六除之即得。
答曰： a斤 b 两 c銖 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The solution involves calculating the amount of silk (in units of "斤", "两", and "銖") that each household is responsible for. Let's compute this step by step.


"""


from fractions import Fraction

# Total silk in various units
total_silk_stone = 8  # 石
total_silk_jin = 5    # 斤
total_silk_liang = 3  # 两
total_silk_zhu = 8    # 銖

# Conversion factors
stone_to_jin = 30
jin_to_liang = 16
liang_to_zhu = 24

# Total households
total_households = 565

# Step 1: Convert everything to 銖 (smallest unit)
total_silk_zhu += total_silk_liang * liang_to_zhu
total_silk_zhu += total_silk_jin * jin_to_liang * liang_to_zhu
total_silk_zhu += total_silk_stone * stone_to_jin * jin_to_liang * liang_to_zhu

# Step 2: Divide the total silk (in 銖) by the number of households
silk_per_household_zhu = Fraction(total_silk_zhu, total_households)

# Step 3: Convert back to 斤, 两, and 銖
a = silk_per_household_zhu // (jin_to_liang * liang_to_zhu)  # 斤
remaining_zhu = silk_per_household_zhu % (jin_to_liang * liang_to_zhu)

b = remaining_zhu // liang_to_zhu  # 两
c = remaining_zhu % liang_to_zhu   # 銖

# Results
a = int(a)
b = int(b)
c = int(c)

# Output variables a, b, c
a, b, c


"""


### Explanation:
1. **Conversion to 銖**: All units are converted to the smallest unit (銖) using the given conversion factors.
2. **Division by households**: The total silk in 銖 is divided by the number of households to find the amount of silk per household in 銖.
3. **Conversion back to larger units**: The result in 銖 is converted back to 斤, 两, and 銖 using integer division and modulo operations.

### Final Output:
The variables `a`, `b`, and `c` will contain the number of 斤, 两, and 銖 of silk per household, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 0
Variable 'b' has wrong value. Expected: 11, Actual: 6
Variable 'c' has wrong value. Expected: 8, Actual: 22"""
