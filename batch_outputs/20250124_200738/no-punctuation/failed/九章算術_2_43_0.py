"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤銖率之問各幾何
反其率術曰以錢數為法所率為實實如法而一不滿法者反以實減法法少實多二物各以所得多少之數乘法實即物數
荅曰其 a鈞  b銖 一錢 其 c石  d銖 一錢
"""

"""
This problem is complex and involves ancient Chinese units of measurement and their relationships. Let's break it down step by step and translate the procedure into Python code.

### Problem Explanation:
- You have spent **13,970 qian** to buy **1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu** of silk.
- You want to calculate the price per zhu (銖 rate) and determine how much silk corresponds to one qian (monetary unit).

### Procedure ("反其率術"):
1. Take the total money spent as the divisor (法, "the rule").
2. Take the total weight of silk as the dividend (實, "the reality").
3. Divide the dividend by the divisor to get the rate per unit.
4. If the divisor is less than the dividend, invert the calculation and adjust accordingly.
5. Use the calculated rate to determine the amount of silk corresponding to one qian.

### Units Conversion:
- 1 shi (石) = 4 jun (鈞)
- 1 jun (鈞) = 30 jin (斤)
- 1 jin (斤) = 16 liang (兩)
- 1 liang (兩) = 24 zhu (銖)

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Total money spent
錢數 = 13970

# Total weight of silk in ancient units
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Convert all units to zhu (銖)
總銖數 = (
    石 * 4 * 30 * 16 * 24 +  # Convert 石 to 銖
    鈞 * 30 * 16 * 24 +      # Convert 鈞 to 銖
    斤 * 16 * 24 +           # Convert 斤 to 銖
    兩 * 24 +                # Convert 兩 to 銖
    銖                      # Add 銖
)

# Step 1: Take the total money as the divisor (法) and total weight as the dividend (實)
法 = 錢數
實 = 總銖數

# Step 2: Calculate the rate per 銖
銖率 = Fraction(實, 法)

# Step 3: Determine the amount of silk corresponding to one qian
# Multiply the rate by 1 qian (1 unit of money)
一錢絲量 = 銖率

# Convert the result back into traditional units
# Start with the total zhu (銖) and work backwards
總銖 = 一錢絲量

# Convert 銖 to 兩
兩 = 總銖 // 24
剩餘銖 = 總銖 % 24

# Convert 兩 to 斤
斤 = 兩 // 16
剩餘兩 = 兩 % 16

# Convert 斤 to 鈞
鈞 = 斤 // 30
剩餘斤 = 斤 % 30

# Convert 鈞 to 石
石 = 鈞 // 4
剩餘鈞 = 鈞 % 4

# Final Answer
a = 石
b = 剩餘鈞
c = 剩餘斤
d = 剩餘兩
e = 剩餘銖

print(f"其 {a}石 {b}鈞 {c}斤 {d}兩 {e}銖 一錢")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Unit Conversion**: All the given weights are converted into the smallest unit, `zhu (銖)`, for easier calculations.
2. **Rate Calculation**: The rate per `zhu` is calculated by dividing the total weight (`實`) by the total money spent (`法`).
3. **Reverse Calculation**: Using the rate, the amount of silk corresponding to one qian is calculated.
4. **Unit Conversion Back**: The result is converted back into the traditional units (`石`, `鈞`, `斤`, `兩`, `銖`) for the final answer.

### Final Output:
The program will output the amount of silk corresponding to one qian in the format:
```
其 a石 b鈞 c斤 d兩 e銖 一錢
```
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 0
Variable 'b' has wrong value. Expected: 5, Actual: 0
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 0
Variable 'd' has wrong value. Expected: 6, Actual: 0"""
