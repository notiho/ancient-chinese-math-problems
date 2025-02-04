"""
今有出錢一千一百二十買絲一石二鈞十八斤欲其貴賤斤率之問各幾何
其率術曰各置所買石鈞斤兩以為法以所率乘錢數為實實如法而一不滿法者反以實減法法賤實貴
荅曰其 a鈞 斤 b錢 其 c石 斤 d錢 
"""

"""
The problem and procedure you provided are quite complex and involve determining the price per unit weight (jin, shi, etc.) of silk based on the total cost and weight. Let's carefully translate the procedure into Python code step by step.

### Problem Explanation:
- You have spent **1120 qian** to buy **1 shi, 2 jun, and 18 jin** of silk.
- You want to calculate the price per jin (unit weight) and determine the cost for each unit of weight (shi, jun, jin).

### Procedure Explanation:
1. Place the weights (shi, jun, jin, etc.) as the divisor (法).
2. Multiply the total money (錢數) by the respective rates (所率) to get the dividend (實).
3. Divide the dividend by the divisor to get the price per unit weight.
4. If the result is not a whole number, adjust by subtracting or adding as necessary.

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction

# 出錢一千一百二十
錢數 = 1120

# 買絲一石二鈞十八斤
石 = 1
鈞 = 2
斤 = 18

# 各置所買石鈞斤兩以為法
法 = (石 * 120) + (鈞 * 30) + 斤  # 1 石 = 120 斤, 1 鈞 = 30 斤

# 以所率乘錢數為實
實 = 錢數 * 1  # 所率 is 1 since we are calculating the price per jin

# 實如法而一
斤率 = Fraction(實, 法)  # Price per jin

# 不滿法者反以實減法法賤實貴
# (This step adjusts for rounding, but since we use Fraction, it is exact.)

# Calculate the cost for each unit of weight
# 其 a鈞 斤 b錢
a = 鈞
b = 斤率 * 30  # 1 鈞 = 30 斤

# 其 c石 斤 d錢
c = 石
d = 斤率 * 120  # 1 石 = 120 斤

# Output the results
print(f"其 {a} 鈞 斤 {b} 錢")
print(f"其 {c} 石 斤 {d} 錢")
#----- content ends here -----


"""


### Explanation of Variables:
- `法`: The total weight in jin (converted from shi, jun, and jin).
- `實`: The total money spent, multiplied by the rate (in this case, 1 since we are calculating per jin).
- `斤率`: The price per jin, calculated as `實 / 法`.
- `a` and `b`: The cost for 1 jun in qian.
- `c` and `d`: The cost for 1 shi in qian.

### Example Output:
If you run the code, it will calculate the price per jin and the cost for each unit of weight based on the given procedure.
"""


"""
Variable 'a' has wrong value. Expected: 34/15, Actual: 2
Variable 'b' has wrong value. Expected: 5, Actual: 5600/33
Variable 'c' has wrong value. Expected: 13/12, Actual: 1
Variable 'd' has wrong value. Expected: 6, Actual: 22400/33"""
