"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤鈞率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a斤 鈞 b錢 其 c石 鈞 d錢 
"""

"""
This problem involves calculating the price per unit weight (jin and jun) of silk based on the total cost and total weight. Let's break it down step by step according to the procedure.

### Problem:
You have spent 13,970 qian to buy silk weighing 1 shi, 2 jun, 28 jin, 3 liang, and 5 zhu.  
Question: What is the price per jun and per shi?

### Procedure:
1. Place the total weight (in shi, jun, jin, liang, zhu) as the divisor (法).
2. Multiply the total cost (錢數) by the rate (所率) to get the dividend (實).
3. Divide the dividend by the divisor to get the price per unit.
4. If there is a remainder, adjust accordingly.

### Answer:
The price per jin and jun is *a* qian, and the price per shi and jun is *c* qian.

Now, let's implement this in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Total cost in qian
錢數 = 13970

# Total weight in shi, jun, jin, liang, zhu
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors
一石 = 120  # 1 石 = 120 鈞
一鈞 = 30   # 1 鈞 = 30 斤
一斤 = 16   # 1 斤 = 16 兩
一兩 = 24   # 1 兩 = 24 銖

# Convert total weight to 銖 (smallest unit)
總銖 = (石 * 一石 * 一鈞 * 一斤 * 一兩) + (鈞 * 一鈞 * 一斤 * 一兩) + (斤 * 一斤 * 一兩) + (兩 * 一兩) + 銖

# Convert total weight to 鈞 (for 鈞 rate)
總鈞 = Fraction(總銖, 一鈞 * 一斤 * 一兩)

# Convert total weight to 石 (for 石 rate)
總石 = Fraction(總銖, 一石 * 一鈞 * 一斤 * 一兩)

# Calculate price per 鈞
每鈞價 = Fraction(錢數, 總鈞)

# Calculate price per 石
每石價 = Fraction(錢數, 總石)

# Results
a = 每鈞價  # Price per 鈞
c = 每石價  # Price per 石

print(f"其 {a} 錢 鈞")
print(f"其 {c} 錢 石")
#----- content ends here -----


"""


### Explanation:
1. **Weight Conversion**: The total weight is converted into the smallest unit (zhu) for precise calculations.
2. **Divisor (法)**: The total weight in jun and shi is used as the divisor.
3. **Dividend (實)**: The total cost is divided by the weight to calculate the price per unit.
4. **Results**: The price per jun and per shi is calculated and displayed.

Let me know if you'd like further clarification!
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 160934400/1416269
Missing variable in output: 'b'
Variable 'c' has wrong value. Expected: 19253/11520, Actual: 19312128000/1416269
Missing variable in output: 'd'"""
