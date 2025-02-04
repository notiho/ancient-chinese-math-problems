"""
今有出錢一萬三千九百七十買絲一石二鈞二十八斤三兩五銖欲其貴賤斤率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a石 斤 b錢 其 c斤 斤 d錢 
"""

"""
To solve this problem, we need to calculate the price per unit weight of silk (斤, jin) based on the total cost and total weight. The problem involves converting the weight into a unified unit (jin) and then dividing the total cost by the total weight to determine the price per jin. Here's the step-by-step solution encoded in Python:


"""

#----- content starts here -----

from fractions import Fraction

# 出錢一萬三千九百七十
錢數 = 13970

# 買絲一石二鈞二十八斤三兩五銖
石 = 1
鈞 = 2
斤 = 28
兩 = 3
銖 = 5

# 1 石 = 120 斤, 1 鈞 = 30 斤, 1 斤 = 16 兩, 1 兩 = 24 銖
# Convert the total weight to 銖 (the smallest unit)
總銖 = (石 * 120 * 16 * 24) + (鈞 * 30 * 16 * 24) + (斤 * 16 * 24) + (兩 * 24) + 銖

# Convert the total weight to 斤 (the base unit for price calculation)
總斤 = Fraction(總銖, 16 * 24)

# Calculate the price per 斤
每斤價錢 = Fraction(錢數, 總斤)

# Extract the integer part (石, 鈞, 斤) and fractional part (兩, 銖) of the price
# Convert the price per 斤 back to 銖 for detailed breakdown
每斤價錢銖 = 每斤價錢 * 16 * 24

# Calculate 石, 鈞, 斤, 兩, 銖 for the price
價石 = 每斤價錢銖 // (120 * 16 * 24)
剩餘銖 = 每斤價錢銖 % (120 * 16 * 24)

價鈞 = 剩餘銖 // (30 * 16 * 24)
剩餘銖 %= (30 * 16 * 24)

價斤 = 剩餘銖 // (16 * 24)
剩餘銖 %= (16 * 24)

價兩 = 剩餘銖 // 24
價銖 = 剩餘銖 % 24

# Output the results
a = int(價石)
b = int(價鈞)
c = int(價斤)
d = Fraction(價兩 * 24 + 價銖, 24)

print(f"其 {a} 石 {b} 鈞 {c} 斤 {d} 錢")
#----- content ends here -----


"""
 

### Explanation:
1. **Weight Conversion**: Convert the total weight into 銖 (the smallest unit) and then into 斤 (the base unit for price calculation).
2. **Price Calculation**: Divide the total cost by the total weight in 斤 to get the price per 斤.
3. **Breakdown**: Convert the price per 斤 into 石, 鈞, 斤, 兩, and 銖 for detailed representation.
4. **Output**: The result is displayed in the format specified in the problem.
"""


"""
Variable 'a' has wrong value. Expected: 18013/11520, Actual: 0
Variable 'b' has wrong value. Expected: 67, Actual: 2
Variable 'c' has wrong value. Expected: 7897/384, Actual: 7
Variable 'd' has wrong value. Expected: 68, Actual: 126352/79949"""
