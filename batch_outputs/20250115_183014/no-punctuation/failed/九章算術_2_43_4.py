"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤銖率之問各幾何
反其率術曰以錢數為法所率為實實如法而一不滿法者反以實減法法少實多二物各以所得多少之數乘法實即物數
荅曰其 a鈞  b銖 一錢 其 c石  d銖 一錢
"""

"""
This problem involves calculating the price per unit weight (銖 rate) of silk based on the total money spent and the total weight of silk purchased. The procedure involves reversing the rate to determine the price per unit weight.

### Problem Breakdown:
- Total money spent: 13,970 (錢)
- Total weight of silk: 1 石, 2 鈞, 28 斤, 3 兩, 5 銖
- Question: What is the price per 銖 (銖 rate)?

### Procedure:
1. Use the total money as the divisor (法).
2. Use the total weight as the dividend (實).
3. Divide the dividend by the divisor to determine the rate.
4. If the result is not an integer, adjust by reversing the calculation to ensure the rate is accurate.

### Conversion Factors:
- 1 石 = 4 鈞
- 1 鈞 = 30 斤
- 1 斤 = 16 兩
- 1 兩 = 24 銖

### Step-by-Step Solution:


"""


from fractions import Fraction

# Total money spent
錢數 = 13970

# Total weight of silk in 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Convert total weight to 銖
總銖 = (石 * 4 * 30 * 16 * 24) + (鈞 * 30 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# Reverse the rate: 銖 rate = Total money / Total weight
銖率 = Fraction(錢數, 總銖)

# Convert 銖 rate back to larger units for clarity
# Find 鈞 and remaining 銖
a = 銖率.numerator // (30 * 16 * 24)  # 鈞
remaining_銖 = 銖率.numerator % (30 * 16 * 24)

# Find 銖 and remaining 錢
b = remaining_銖 // 24  # 銖
remaining_錢 = remaining_銖 % 24

# Find 石 and remaining 銖
c = 銖率.numerator // (4 * 30 * 16 * 24)  # 石
remaining_銖_2 = 銖率.numerator % (4 * 30 * 16 * 24)

# Find 銖 and remaining 錢 for 石
d = remaining_銖_2 // 24  # 銖
remaining_錢_2 = remaining_銖_2 % 24

# Output the results
print(f"其 {a} 鈞 {b} 銖 一錢")
print(f"其 {c} 石 {d} 銖 一錢")


"""
 

This code calculates the price per 銖 (銖 rate) and expresses it in terms of larger units (鈞 and 石) for clarity. The results are printed as per the problem's requirements.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 1
Variable 'b' has wrong value. Expected: 5, Actual: 102
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 0
Variable 'd' has wrong value. Expected: 6, Actual: 582"""
