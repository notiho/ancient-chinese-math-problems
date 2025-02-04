"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤銖率之問各幾何
反其率術曰以錢數為法所率為實實如法而一不滿法者反以實減法法少實多二物各以所得多少之數乘法實即物數
荅曰其 a鈞  b銖 一錢 其 c石  d銖 一錢
"""

"""
This problem involves calculating the price per unit weight (銖 rate) for silk, given the total cost and total weight. The procedure involves reversing the rate to find the price per unit and then calculating the distribution of the cost across the weights.

Let's break it down step by step:

### Problem:
You have spent 13,970 units of money to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu. The task is to calculate the price per zhu (銖 rate) and distribute the cost accordingly.

### Procedure:
1. Use the total money as the divisor (法).
2. Use the total weight as the dividend (實).
3. Divide the dividend by the divisor to find the rate.
4. If the divisor is not a perfect multiple of the dividend, adjust by reversing the calculation.
5. Multiply the resulting rate by the weight of each unit (石, 鈞, etc.) to distribute the cost.

### Units Conversion:
1 石 = 4 鈞  
1 鈞 = 30 斤  
1 斤 = 16 兩  
1 兩 = 24 銖  

### Code Implementation:

"""


from fractions import Fraction

# Total money spent
錢數 = 13970

# Total weight in terms of 石, 鈞, 斤, 兩, 銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Convert all weights to 銖
總銖 = (石 * 4 * 30 * 16 * 24) + (鈞 * 30 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# Use the total money as the divisor (法) and total weight as the dividend (實)
法 = 錢數
實 = 總銖

# Calculate the rate per 銖
銖率 = Fraction(實, 法)

# Reverse the calculation to distribute the cost
# Calculate the cost for each unit
石錢 = 銖率 * (石 * 4 * 30 * 16 * 24)
鈞錢 = 銖率 * (鈞 * 30 * 16 * 24)
斤錢 = 銖率 * (斤 * 16 * 24)
兩錢 = 銖率 * (兩 * 24)
銖錢 = 銖率 * 銖

# Convert the results back to the appropriate units
a = Fraction(鈞錢, 1)  # 鈞
b = Fraction(銖錢, 1)  # 銖
c = Fraction(石錢, 1)  # 石
d = Fraction(銖錢, 1)  # 銖

# Output the results
print(f"其 {a} 鈞 {b} 銖 一錢")
print(f"其 {c} 石 {d} 銖 一錢")


"""


This code calculates the price per unit weight (銖 rate) and distributes the cost across the weights, providing the results in terms of 鈞 and 銖.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 184202496/1397
Variable 'b' has wrong value. Expected: 5, Actual: 79949/2794
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 368404992/1397
Variable 'd' has wrong value. Expected: 6, Actual: 79949/2794"""
