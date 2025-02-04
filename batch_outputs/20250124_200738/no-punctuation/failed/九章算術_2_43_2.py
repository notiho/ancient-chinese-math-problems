"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤銖率之問各幾何
反其率術曰以錢數為法所率為實實如法而一不滿法者反以實減法法少實多二物各以所得多少之數乘法實即物數
荅曰其 a鈞  b銖 一錢 其 c石  d銖 一錢
"""

"""
This is a complex ancient Chinese problem involving proportional relationships and unit conversions. Let's break it down and translate it into Python code step by step.

### Problem Breakdown:
- **Given**:  
  - Money spent: 13,970 qian  
  - Silk purchased: 1 shi, 2 jun, 28 jin, 3 liang, 5 zhu  
- **Goal**:  
  - Determine the price per zhu (銖 rate).  
  - Use the reverse rate procedure to calculate the proportional amounts for each unit.

### Procedure Explanation:
1. **Reverse Rate Procedure**:  
   - Use the total money as the divisor (法).  
   - Use the total weight of silk as the dividend (實).  
   - Divide the dividend by the divisor to find the rate per unit.  
   - If the divisor is not a perfect multiple of the dividend, adjust accordingly.  
2. **Unit Conversion**:  
   - 1 shi = 4 jun  
   - 1 jun = 30 jin  
   - 1 jin = 16 liang  
   - 1 liang = 24 zhu  

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
錢數 = 13970  # Total money spent
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Unit conversions to total zhu
銖總數 = (石 * 4 * 30 * 16 * 24) + (鈞 * 30 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# Reverse rate procedure
法 = 錢數  # Total money as the divisor
實 = 銖總數  # Total zhu as the dividend

# Calculate the rate per zhu
銖率 = Fraction(實, 法)

# Outputs
a = 銖率.numerator  # Numerator of the rate (price per zhu)
b = 銖率.denominator  # Denominator of the rate (price per zhu)

# Convert back to larger units for clarity
# Calculate the total silk amount in shi, jun, jin, liang, zhu
總石 = 銖總數 // (4 * 30 * 16 * 24)
剩餘銖 = 銖總數 % (4 * 30 * 16 * 24)

總鈞 = 剩餘銖 // (30 * 16 * 24)
剩餘銖 %= (30 * 16 * 24)

總斤 = 剩餘銖 // (16 * 24)
剩餘銖 %= (16 * 24)

總兩 = 剩餘銖 // 24
剩餘銖 %= 24

總銖 = 剩餘銖

# Final outputs
c = 總石
d = 總銖

print(f"其 {a}鈞 {b}銖 一錢")
print(f"其 {c}石 {d}銖 一錢")
#----- content ends here -----


"""


### Explanation of Variables:
- `銖總數`: Total weight of silk in zhu.  
- `法`: Total money spent (divisor).  
- `實`: Total weight of silk (dividend).  
- `銖率`: Rate per zhu (as a fraction).  
- `總石`, `總鈞`, `總斤`, `總兩`, `總銖`: Breakdown of the total silk weight into larger units.

### Final Answer:
The output will provide the rate per zhu and the breakdown of the silk weight into shi, jun, jin, liang, and zhu.
"""


"""
Variable 'a' has wrong value. Expected: 3871/2304, Actual: 79949
Variable 'b' has wrong value. Expected: 5, Actual: 13970
Variable 'c' has wrong value. Expected: 10099/7680, Actual: 1
Variable 'd' has wrong value. Expected: 6, Actual: 5"""
