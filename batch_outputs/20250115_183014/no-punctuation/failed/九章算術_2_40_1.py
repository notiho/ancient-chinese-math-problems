"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤鈞率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a斤 鈞 b錢 其 c石 鈞 d錢 
"""

"""
This problem is complex and involves calculating the price per unit weight (jin and jun) for silk based on the total cost and weight. Let's break it down step by step and encode the procedure in Python.

### Problem Explanation:
- Total money spent: 13,970 (in qian).
- Total weight of silk: 1 shi, 2 jun, 28 jin, 3 liang, 5 zhu.
- The goal is to calculate the price per jun (鈞) and per jin (斤).

### Procedure:
1. Place the total weight (in shi, jun, jin, liang, zhu) as the divisor (法).
2. Multiply the total money (錢數) by the rate (所率) to get the dividend (實).
3. Divide the dividend by the divisor to get the price per unit.
4. If there is a remainder, adjust the calculation as needed.

### Python Code:


"""


from fractions import Fraction

# Total money spent
錢數 = 13970

# Total weight in various units
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# Conversion factors (1 石 = 4 鈞, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖)
石_to_鈞 = 4
鈞_to_斤 = 30
斤_to_兩 = 16
兩_to_銖 = 24

# Convert total weight to a single unit (銖)
總銖 = (
    石 * 石_to_鈞 * 鈞_to_斤 * 斤_to_兩 * 兩_to_銖 +
    鈞 * 鈞_to_斤 * 斤_to_兩 * 兩_to_銖 +
    斤 * 斤_to_兩 * 兩_to_銖 +
    兩 * 兩_to_銖 +
    銖
)

# Conversion factors for 鈞 and 斤
銖_per_斤 = 斤_to_兩 * 兩_to_銖
銖_per_鈞 = 鈞_to_斤 * 銖_per_斤

# Calculate price per 鈞 (貴)
貴_per_鈞 = Fraction(錢數, 總銖) * 銖_per_鈞

# Calculate price per 斤 (賤)
賤_per_斤 = Fraction(錢數, 總銖) * 銖_per_斤

# Convert results to integers and fractions
a = 貴_per_鈞
b = 賤_per_斤

print(f"其 {a} 鈞 錢")
print(f"其 {b} 斤 錢")


"""


### Explanation of the Code:
1. **Weight Conversion**: The total weight is converted into the smallest unit (銖) using the given conversion factors.
2. **Price Calculation**: The price per 鈞 and per 斤 is calculated by dividing the total money by the total weight in 銖, then multiplying by the respective conversion factors.
3. **Output**: The results are expressed as fractions to ensure precision.

### Answer:
- The price per 鈞 is `a` qian.
- The price per 斤 is `b` qian.
"""


"""
Variable 'a' has wrong value. Expected: 979/128, Actual: 160934400/79949
Variable 'b' has wrong value. Expected: 2012, Actual: 5364480/79949
Missing variable in output: 'c'
Missing variable in output: 'd'"""
